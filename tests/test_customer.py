from uuid import uuid4

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_customer():
    response = client.post(
        "/customers/",
        json={
            "name": "Test Customer",
            "email": f"test.{uuid4()}@portfolio.com",
            "company": "Test Company",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Test Customer"
    assert data["email"].endswith("@portfolio.com")
    assert data["company"] == "Test Company"


def test_get_customer_not_found():
    response = client.get("/customers/99999")

    assert response.status_code == 404


def test_update_customer():
    response = client.put(
        "/customers/3",
        json={
            "name": "Updated Test Customer",
            "email": "updated.test@portfolio.com",
            "company": "Updated Test Company",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Updated Test Customer"
    assert data["email"] == "updated.test@portfolio.com"


def test_update_customer_duplicate_email():
    response = client.put(
        "/customers/3",
        json={
            "name": "Duplicate Test",
            "email": "user@example.com",
            "company": "Conflict Test Inc",
        },
    )

    assert response.status_code == 409