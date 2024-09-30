from pydantic import BaseModel, Field
from typing import Optional


# Books : Model
class Book:
    id:int
    title:str
    author:str
    description:str
    rating:int
    published_date:int

    def __init__(self,id,title,author,description,rating, published_date):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating
        self.published_date=published_date


# Pydantic Model for data validating over Book
class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed", default=None)
    title:str = Field(min_length=3)
    author:str = Field(min_length=1)
    description:str = Field(min_length=1, max_length=200)
    rating:int = Field(gt=-1, lt=6)
    published_date:int = Field(gt=1900, lt=2030)

    model_config = {
        "json_schema_extra" : {
            "example" : {
            "title":"Book_name",
            "author":"Book_author",
            "description":"Book_description",
            "rating":5,
            "published_date":2029
            }
        }
    }


# BOOKS list
BOOKS = [
    Book(1, "To Kill a Mockingbird", "Harper Lee", "A novel about the injustices of racism in the American South.", 5,1999),
    Book(2, "1984", "George Orwell", "A dystopian novel set in a totalitarian society under constant surveillance.", 5, 1980),
    Book(3, "The Great Gatsby", "F. Scott Fitzgerald", "A story about the American dream and the downfall of those who attempt to reach its illusionary goals.", 4,2002),
    Book(4, "Moby-Dick", "Herman Melville", "The tale of a sea captain's obsession with a white whale.", 4,2003),
    Book(5, "Pride and Prejudice", "Jane Austen", "A romantic novel that critiques the British class system of the early 19th century.", 5, 2005),
    Book(6, "The Catcher in the Rye", "J.D. Salinger", "A novel about teenage angst and alienation.", 4, 2020),
    Book(7, "The Hobbit", "J.R.R. Tolkien", "A fantasy adventure about a hobbit's journey to recover treasure guarded by a dragon.", 5, 2005),
    Book(8, "War and Peace", "Leo Tolstoy", "A novel that chronicles the French invasion of Russia and its impact on society.", 5, 2020),
    Book(9, "The Alchemist", "Paulo Coelho", "A philosophical novel about a young shepherd's journey to find his personal legend.", 4, 1989),
    Book(10, "Brave New World", "Aldous Huxley", "A dystopian novel that explores a world of technological advancements and controlled societies.", 5, 1980),
]

