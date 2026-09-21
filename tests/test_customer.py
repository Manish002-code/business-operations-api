from uuid import uuid4

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_customer():
    email = f"test.{uuid4()}@portfolio.com"

    response = client.post(
        "/customers/",
        json={
            "name": "Test Customer",
            "email": email,
            "company": "Test Company",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Test Customer"
    assert data["email"] == email
    assert data["company"] == "Test Company"


def test_get_customer_not_found():
    response = client.get("/customers/999999")

    assert response.status_code == 404


def test_update_customer():
    email = f"update.{uuid4()}@portfolio.com"

    create_response = client.post(
        "/customers/",
        json={
            "name": "Update Test Customer",
            "email": email,
            "company": "Update Test Company",
        },
    )

    assert create_response.status_code == 201

    customer_id = create_response.json()["id"]

    response = client.put(
        f"/customers/{customer_id}",
        json={
            "name": "Updated Test Customer",
            "email": f"updated.{uuid4()}@portfolio.com",
            "company": "Updated Test Company",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Updated Test Customer"
    assert data["company"] == "Updated Test Company"


def test_update_customer_duplicate_email():
    email = f"duplicate.{uuid4()}@portfolio.com"

    first_response = client.post(
        "/customers/",
        json={
            "name": "Existing Customer",
            "email": email,
            "company": "Existing Company",
        },
    )

    assert first_response.status_code == 201

    second_response = client.post(
        "/customers/",
        json={
            "name": "Second Customer",
            "email": f"second.{uuid4()}@portfolio.com",
            "company": "Second Company",
        },
    )

    assert second_response.status_code == 201

    second_customer_id = second_response.json()["id"]

    response = client.put(
        f"/customers/{second_customer_id}",
        json={
            "name": "Duplicate Test",
            "email": email,
            "company": "Conflict Test Inc",
        },
    )

    assert response.status_code == 409


def test_delete_customer():
    email = f"delete.{uuid4()}@portfolio.com"

    create_response = client.post(
        "/customers/",
        json={
            "name": "Delete Test Customer",
            "email": email,
            "company": "Delete Company",
        },
    )

    assert create_response.status_code == 201

    customer_id = create_response.json()["id"]

    response = client.delete(f"/customers/{customer_id}")

    assert response.status_code == 200

    get_response = client.get(f"/customers/{customer_id}")

    assert get_response.status_code == 404