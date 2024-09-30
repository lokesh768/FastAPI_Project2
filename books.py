from fastapi import FastAPI, Path, Query, HTTPException
from book import Book, BookRequest, BOOKS
from starlette import status

app = FastAPI()


# GET method
@app.get('/books',status_code=status.HTTP_200_OK)
async def fech_books():
    return BOOKS

# GET method for fetching book by id
@app.get('/books/{book_id}',status_code=status.HTTP_200_OK)
async def get_book(book_id:int=Path(gt=0)):
    for book in BOOKS:
        if book.id==book_id:
            return book
    raise HTTPException(status_code=404,detail='Item Not found')


# GET method to fetch books by rating   
@app.get('/books/',status_code=status.HTTP_200_OK)
async def fetch_books_by_rating(book_rating:int=Query(lt=6,gt=0)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

# GET method to fetch books by published date
@app.get('/books/published-date/',status_code=status.HTTP_200_OK)
async def fetch_books_by_published_date(published_date:int=Query(gt=1900, lt=2030)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date==published_date:
            books_to_return.append(book)
    return books_to_return


# POST method with data validation
@app.post('/books/add_book',status_code=status.HTTP_201_CREATED)
async def add_book(book_request:BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))

# for adding id to the book
def find_book_id(book:Book):
    book.id = 1 if len(BOOKS)==0 else BOOKS[-1].id +1
    return book


# PUT method
@app.put('/books/update_book',status_code=status.HTTP_204_NO_CONTENT)
async def update_book(updated_book:BookRequest):
    book_changed = False
    book = Book(**updated_book.model_dump())
    for i in range(len(BOOKS)):
        if BOOKS[i].id==book.id:
            BOOKS[i]=book
            book_changed=True
    if not book_changed:
        raise HTTPException(status_code=404,detail='Item Not Found')

# DELETE method
@app.delete('/books/delete_book/{book_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int=Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id==book_id:
            BOOKS.pop(i)
            book_changed=True
            break
    if not book_changed:
        raise HTTPException(status_code=404,detail='Item Not Found')