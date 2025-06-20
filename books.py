from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID, uuid4

app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)
    
# Static books data
BOOKS = [
    Book(
        id=uuid4(),
        title="The Great Gatsby",
        author="F. Scott Fitzgerald",
        description="A classic novel set in the Jazz Age.",
        rating=90
    ),
    Book(
        id=uuid4(),
        title="To Kill a Mockingbird",
        author="Harper Lee",
        description="A profound story about justice and race.",
        rating=95
    ),
    Book(
        id=uuid4(),
        title="1984",
        author="George Orwell",
        description="A dystopian novel about totalitarianism.",
        rating=92
    ),
    Book(
        id=uuid4(),
        title="Pride and Prejudice",
        author="Jane Austen",
        description="A romantic story with sharp social commentary.",
        rating=89
    ),
    Book(
        id=uuid4(),
        title="The Catcher in the Rye",
        author="J.D. Salinger",
        description="A tale of teenage angst and rebellion.",
        rating=85
    )
]


@app.get("/books")
def read_root():
    return BOOKS


@app.post("/")
def create_book(book: Book):
    BOOKS.append(book)
    return BOOKS
