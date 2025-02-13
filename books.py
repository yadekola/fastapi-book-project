from fastapi import APIRouter, HTTPException

router = APIRouter()

# Dummy data (you might be using a database instead)
books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
]

@router.get("/api/v1/books/{book_id}")
def get_book(book_id: int):
    """
    Retrieve a book by its ID.

    - If found, return book details.
    - If not found, return 404 Not Found.
    """
    for book in books:
        if book["id"] == book_id:
            return book
    
    # If the book is not found, return 404 response
    raise HTTPException(status_code=404, detail="Book not found")
