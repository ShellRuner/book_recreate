from uuid import UUID, uuid4
from fastapi import params, HTTPException
from fastapi.testclient import TestClient
from routers import book 
from routers.book import book_router
from database import books
from schemas.book import BookCreate, Response
# from main import app


client = TestClient(book_router)

#Book list test
def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert response.json() == books

#Test the get book by id endpoint
def test_get_book_by_id():
    
    id = uuid4()
    response = client.get(f"/books/{id}").json()
    assert response.get("status_code") == 404
    assert response.get("message") == "book not found"

# #Test the add book endpoint
# book_test = BookCreate(
#     title = "Harry potter",
#     author = "j.k Rowling",
#     year = 1900,
#     language = "english",
#     pages = 345
# )

# def test_add_book():
#     response = client.post("/books", json=book_test.model_dump())
#     print(response.json())
#     response.status_code == 200
#     assert response.json()["message"] == "Book added successfully"
#     assert response.json()["data"]["title"] == "Harry potter"

# # test_add_book()
    
    
    

    
    
    