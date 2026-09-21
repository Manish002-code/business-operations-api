# Business Operations REST API

A production-style REST API built with **Python, FastAPI, PostgreSQL, Pydantic, and SQLAlchemy** for managing business customers.

This is a **personal portfolio project** demonstrating backend API development, database integration, validation, error handling, automated testing, and API documentation.

## 🚀 Features

- RESTful API architecture
- Customer CRUD operations
- PostgreSQL database integration
- SQLAlchemy ORM
- Pydantic request/response validation
- Email validation
- Duplicate email detection
- Proper HTTP status codes
- 404 handling for missing customers
- Health-check endpoint
- Interactive Swagger/OpenAPI documentation
- Automated pytest test suite
- Environment-based configuration

## 🏗️ Architecture

```text
Client
   │
   ▼
FastAPI
   │
   ├── Pydantic Validation
   │
   ├── Business Logic
   │
   └── SQLAlchemy
          │
          ▼
     PostgreSQL

## Project Architecture

business_operations_api/
│
├── app/
│   ├── core/
│   │   └── config.py
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── customer.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── customer.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── customer_service.py
│   │
│   ├── __init__.py
│   └── main.py
│
├── tests/
│   ├── __init__.py
│   └── test_customer.py
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt

## 🔌 API Endpoints

### Health Check

```http
GET /health
Returns the current API health status.

Example response:

{
  "status": "healthy"
}
Customer Endpoints
Method	Endpoint	Description
GET	/customers/	List all customers
POST	/customers/	Create a customer
GET	/customers/{customer_id}	Get a customer
PUT	/customers/{customer_id}	Update a customer
DELETE	/customers/{customer_id}	Delete a customer
🧪 API Validation & Error Handling

The API handles common business scenarios using appropriate HTTP status codes.

Successful Customer Creation
201 Created

Example:

{
  "id": 6,
  "name": "Portfolio API Customer",
  "email": "portfolio.customer@demo.com",
  "company": "Demo Analytics Inc"
}
Duplicate Email

If a customer is created using an email address that already exists:

409 Conflict

Example:

{
  "detail": "Customer email already exists"
}
Customer Not Found

If a requested customer ID does not exist:

404 Not Found

Example:

{
  "detail": "Customer not found"
}
Validation Error

Invalid request data returns:

422 Unprocessable Entity

FastAPI and Pydantic automatically provide detailed validation information.

📖 Interactive API Documentation

The application automatically generates interactive Swagger/OpenAPI documentation.

Open:

http://127.0.0.1:8000/docs

The raw OpenAPI specification is available at:

http://127.0.0.1:8000/openapi.json

The Swagger interface was used to test:

Health check
Customer creation
Customer listing
Customer retrieval
Customer update
Customer deletion
Duplicate email handling
Customer-not-found handling
🧪 Automated Testing

The project uses pytest for automated testing.

Current test result:

4 passed

Tests cover important customer API behavior including:

Customer creation
Duplicate email handling
Customer retrieval
Customer update
Customer deletion
Request validation

Run the test suite with:

pytest -q
🛠️ Technology Stack
Backend
Python
FastAPI
Uvicorn
Database
PostgreSQL
SQLAlchemy
Validation
Pydantic
Email validation
Testing
pytest
FastAPI TestClient
Development
Python virtual environment
Git
GitHub
▶️ Running Locally
1. Create and activate the virtual environment

Windows PowerShell:

.venv\Scripts\Activate.ps1
2. Install dependencies
pip install -r requirements.txt
3. Start the API
uvicorn app.main:app --reload
4. Open the API documentation

Open this address in your browser:

http://127.0.0.1:8000/docs
💼 Portfolio Purpose

This is a personal portfolio project created to demonstrate practical Python backend development skills.

The project demonstrates:

Python application development
REST API design
CRUD operations
PostgreSQL integration
SQLAlchemy ORM
Request and response validation
Error handling
Duplicate detection
Automated testing
Interactive API documentation
Production-oriented project structure
🔮 Future Improvements

Potential future enhancements include:

JWT authentication
Role-based access control
Pagination and filtering
Customer search
Order management
Structured application logging
Docker containerization
CI/CD with GitHub Actions
Cloud deployment
API rate limiting
Monitoring and observability
👨‍💻 Project Type

Personal Portfolio Project

Built to demonstrate hands-on Python backend, REST API, PostgreSQL, and application development skills.

