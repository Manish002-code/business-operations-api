from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.customer import CustomerCreate, CustomerUpdate, CustomerResponse
from app.services.customer_service import (
    create_customer,
    get_customers,
    get_customer,
    delete_customer,
    update_customer,
)


router = APIRouter(
    prefix="/customers",
    tags=["Customers"],
)


@router.post(
    "/",
    response_model=CustomerResponse,
    status_code=201,
    responses={
        409: {"description": "Customer email already exists"},
    },
)
def create_customer_endpoint(
    customer: CustomerCreate,
    db: Session = Depends(get_db),
):
    try:
        return create_customer(db, customer)
    except ValueError as exc:
        raise HTTPException(
            status_code=409,
            detail=str(exc),
        )

@router.get(
    "/",
    response_model=list[CustomerResponse],
)
def list_customers(
    db: Session = Depends(get_db),
):
    return get_customers(db)


@router.get(
    "/{customer_id}",
    response_model=CustomerResponse,
    responses={
        404: {"description": "Customer not found"},
    },
)
def get_customer_endpoint(
    customer_id: int,
    db: Session = Depends(get_db),
):
    customer = get_customer(db, customer_id)

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found",
        )

    return customer


@router.delete(
    "/{customer_id}",
    response_model=CustomerResponse,
    responses={
        404: {"description": "Customer not found"},
    },
)
def delete_customer_endpoint(
    customer_id: int,
    db: Session = Depends(get_db),
):
    customer = delete_customer(db, customer_id)

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found",
        )

    return customer

@router.put(
    "/{customer_id}",
    response_model=CustomerResponse,
    responses={
        404: {"description": "Customer not found"},
        409: {"description": "Customer email already exists"},
    },
)
def update_customer_endpoint(
    customer_id: int,
    customer: CustomerUpdate,
    db: Session = Depends(get_db),
):
    try:
        updated_customer = update_customer(
            db,
            customer_id,
            customer
        )

        if not updated_customer:
            raise HTTPException(
                status_code=404,
                detail="Customer not found"
            )

        return updated_customer

    except ValueError as exc:
        raise HTTPException(
            status_code=409,
            detail=str(exc)
        )