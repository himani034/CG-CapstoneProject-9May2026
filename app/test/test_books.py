from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_add_book():

    response = client.post(
        "/books/",
        json={
            "title": "Test Book",
            "author": "Test Author",
            "isbn": "99999",
            "category": "Testing",
            "quantity": 5
        }
    )

    assert response.status_code == 200


def test_get_books():

    response = client.get("/books/")

    assert response.status_code == 200

    assert isinstance(
        response.json(),
        list
    )


