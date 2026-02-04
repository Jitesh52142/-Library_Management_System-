import os
import tempfile
import pytest

from app import app
from model import LibraryModel


@pytest.fixture
def client():
    """
    Creates a test client with a temporary database
    """
    db_fd, db_path = tempfile.mkstemp()

    # Override the model to use test DB
    test_library = LibraryModel(db_name=db_path)

    app.config['TESTING'] = True

    # Monkey-patch the global library object
    import app as flask_app
    flask_app.library = test_library

    with app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(db_path)


def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200


def test_add_book(client):
    response = client.post(
        "/add",
        data={"title": "Test Book", "author": "Test Author"},
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Test Book" in response.data
    assert b"Test Author" in response.data


def test_edit_book(client):
    # Add a book first
    client.post("/add", data={"title": "Old Title", "author": "Author"})

    # Edit the book
    response = client.post(
        "/edit/1",
        data={"title": "New Title", "author": "Author"},
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"New Title" in response.data
    assert b"Old Title" not in response.data


def test_delete_book(client):
    # Add a book first
    client.post("/add", data={"title": "Delete Me", "author": "Author"})

    # Delete the book
    response = client.get("/delete/1", follow_redirects=True)

    assert response.status_code == 200
    assert b"Delete Me" not in response.data
