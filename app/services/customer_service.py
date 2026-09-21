from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.customer import Customer
from app.schemas.customer import CustomerCreate, CustomerUpdate

def create_customer(db: Session, customer: CustomerCreate):
    existing_customer = (
        db.query(Customer)
        .filter(Customer.email == customer.email)
        .first()
    )

    if existing_customer:
        raise ValueError("A customer with this email already exists")

    db_customer = Customer(
        name=customer.name,
        email=customer.email,
        company=customer.company,
    )

    try:
        db.add(db_customer)
        db.commit()
        db.refresh(db_customer)

    except IntegrityError:
        db.rollback()
        raise ValueError("A customer with this email already exists")

    return db_customer

def get_customers(db: Session):
    return db.query(Customer).all()


def get_customer(db: Session, customer_id: int):
    return (
        db.query(Customer)
        .filter(Customer.id == customer_id)
        .first()
    )


def delete_customer(db: Session, customer_id: int):
    customer = get_customer(db, customer_id)

    if customer:
        db.delete(customer)
        db.commit()

    return customer

def update_customer(db: Session, customer_id: int, customer: CustomerUpdate):
    db_customer = get_customer(db, customer_id)

    if not db_customer:
        return None

    existing_customer = (
        db.query(Customer)
        .filter(
            Customer.email == customer.email,
            Customer.id != customer_id
        )
        .first()
    )

    if existing_customer:
        raise ValueError("A customer with this email already exists")

    db_customer.name = customer.name
    db_customer.email = customer.email
    db_customer.company = customer.company

    try:
        db.commit()
        db.refresh(db_customer)
    except IntegrityError:
        db.rollback()
        raise ValueError("A customer with this email already exists")

    return db_customer