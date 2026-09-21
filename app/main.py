from fastapi import FastAPI

from app.api.customers import router as customer_router
from app.db.database import Base, engine

from app.models.customer import Customer


app = FastAPI(
    title="Business Operations API",
    description="REST API for managing business customers with PostgreSQL, validation, duplicate handling, and health monitoring.",
    version="1.0.0",
)


Base.metadata.create_all(bind=engine)


app.include_router(customer_router)


@app.get("/")
def root():
    return {
        "message": "Business Operations API is running",
        "status": "healthy",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }