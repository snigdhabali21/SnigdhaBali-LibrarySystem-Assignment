from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
#from .middleware import middleware

from .database import engine, get_db
from . import models
from .models import Author, Category, Book
from .schemas import AuthorCreate, AuthorResponse, CategoryCreate, CategoryResponse, BookCreate, BookResponse
from sqlalchemy import func

app = FastAPI(title="Library Management API")
# @app.middleware("http")
# async def auth_middleware(request: Request, call_next):
#     return await middleware(request, call_next)

# @app.get("/whoami")
# def whoami(request: Request):
#     return request.state.user

# ---------------- ROUTES FIRST ----------------

@app.get("/")
def root():
    return {"message": "Library API is running"}

@app.post("/authors", response_model=AuthorResponse)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    db_author = Author(name=author.name, bio=author.bio)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

@app.get("/authors", response_model=list[AuthorResponse])
def get_authors(db: Session = Depends(get_db)):
    return db.query(Author).all()

@app.get("/authors/{author_id}", response_model=AuthorResponse)
def get_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(Author).filter(Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@app.put("/authors/{author_id}", response_model=AuthorResponse)
def update_author(
    author_id: int,
    author: AuthorCreate,
    db: Session = Depends(get_db)):
    db_author = db.query(Author).filter(Author.id == author_id).first()

    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")

    db_author.name = author.name
    db_author.bio = author.bio

    db.commit()
    db.refresh(db_author)

    return db_author

@app.delete("/authors/{author_id}")
def delete_author(author_id: int, db: Session = Depends(get_db)):
    db_author = db.query(Author).filter(Author.id == author_id).first()

    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")

    db.delete(db_author)
    db.commit()

    return {"message": "Author deleted successfully"}
#--------------------------Category CRUD----------------------#
@app.post("/categories", response_model=CategoryResponse)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db)
):
    db_category = Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


@app.get("/categories", response_model=list[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()


@app.get("/categories/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@app.put("/categories/{category_id}", response_model=CategoryResponse)
def update_category(
    category_id: int,
    category: CategoryCreate,
    db: Session = Depends(get_db)
):
    db_category = db.query(Category).filter(Category.id == category_id).first()

    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")

    db_category.name = category.name

    db.commit()
    db.refresh(db_category)

    return db_category

@app.delete("/categories/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    db.delete(category)
    db.commit()
    return {"message": "Category deleted successfully"}
#-----------------------Book CRUD---------------------------#
@app.post("/books", response_model=BookResponse)
def create_book(
    book: BookCreate,
    db: Session = Depends(get_db)
):
    # check author exists
    author = db.query(Author).filter(Author.id == book.author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    # check category exists
    category = db.query(Category).filter(Category.id == book.category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    db_book = Book(
        title=book.title,
        isbn=book.isbn,
        publication_year=book.publication_year,
        author_id=book.author_id,
        category_id=book.category_id
    )

    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book

@app.get("/books", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()
@app.get("/books/insights")
def book_insights(db: Session = Depends(get_db)):
    books = db.query(Book).all()

    if not books:
        return {
            "valid_books": [],
            "top_authors": [],
            "busy_years": []
        }

    valid_books = []
    for book in books:
        if (
            book.author is not None and
            book.publication_year is not None and
            1900 <= book.publication_year <= 2100
        ):
            valid_books.append(book)

    author_counts = {}
    for book in valid_books:
        name = book.author.name
        author_counts[name] = author_counts.get(name, 0) + 1

    top_authors = sorted(
        author_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]

    top_authors_result = [
        {"author": name, "book_count": count}
        for name, count in top_authors
    ]

    year_map = {}
    for book in valid_books:
        year = book.publication_year
        year_map.setdefault(year, []).append(book.title)

    busy_years = {
        year: titles
        for year, titles in year_map.items()
        if len(titles) >= 2
    }

    busy_years_sorted = dict(sorted(busy_years.items()))

    return {
        "valid_books": [
            {
                "id": book.id,
                "title": book.title,
                "publication_year": book.publication_year,
                "author": book.author.name
            }
            for book in valid_books
        ],
        "top_authors": top_authors_result,
        "busy_years": busy_years_sorted
    }

# ---------------- Insights report---------------#

@app.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book

@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int,
    book: BookCreate,
    db: Session = Depends(get_db)
):
    db_book = db.query(Book).filter(Book.id == book_id).first()

    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")

   
    author = db.query(Author).filter(Author.id == book.author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    category = db.query(Category).filter(Category.id == book.category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    db_book.title = book.title
    db_book.isbn = book.isbn
    db_book.publication_year = book.publication_year
    db_book.author_id = book.author_id
    db_book.category_id = book.category_id

    db.commit()
    db.refresh(db_book)

    return db_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()

    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(db_book)
    db.commit()

    return {"message": "Book deleted successfully"}
#-----------------Count the books---------------------#
@app.get("/stats/books/count")
def get_total_books(db: Session = Depends(get_db)):
    total_books = db.query(Book).count()
    return {"total_books": total_books}
#----------Avg publication--------------------#
@app.get("/stats/books/average-publication-year")
def get_average_publication_year(db: Session = Depends(get_db)):

    avg_year = db.query(func.avg(Book.publication_year)).scalar()

    if avg_year is None:
        return {
            "average_publication_year": 0,
            "message": "No books available"
        }

    return {
        "average_publication_year": round(avg_year, 2)
    }
#---------------
@app.get("/stats/authors/{author_id}/oldest-newest-books")
def get_oldest_and_newest_books(author_id: int, db: Session = Depends(get_db)):

    books = (
        db.query(Book)
        .filter(Book.author_id == author_id)
        .order_by(Book.publication_year)
        .all()
    )

    if not books:
        return {
            "message": "This author has no books"
        }

    oldest_book = books[0]
    newest_book = books[-1]

    return {
        "author_id": author_id,
        "oldest_book": {
            "title": oldest_book.title,
            "publication_year": oldest_book.publication_year
        },
        "newest_book": {
            "title": newest_book.title,
            "publication_year": newest_book.publication_year
        }
    }
#------------------old and new published book----------#
@app.get("/stats/books/first-n")
def get_first_n_books(
    limit: int = 5,
    db: Session = Depends(get_db)
):
    books = (
        db.query(Book)
        .order_by(Book.title.asc())
        .limit(limit)
        .all()
    )

    return {
        "limit": limit,
        "books": books
    }
#---------------First N-books alphabetically----------------#
@app.get("/stats/categories/{category_id}/publication-year-check")
def check_books_publication_year(category_id: int, db: Session = Depends(get_db)):

    total_books = (
        db.query(Book)
        .filter(Book.category_id == category_id)
        .count()
    )

    if total_books == 0:
        return {
            "category_id": category_id,
            "message": "No books found in this category"
        }

    books_missing_year = (
        db.query(Book)
        .filter(
            Book.category_id == category_id,
            Book.publication_year == None
        )
        .count()
    )

    if books_missing_year > 0:
        return {
            "category_id": category_id,
            "all_books_have_publication_year": False
        }

    return {
        "category_id": category_id,
        "all_books_have_publication_year": True
    }
#------------------do all books in a category have a publication year--------------------#
@app.get("/stats/authors/{author_id}/has-books")
def author_has_books(author_id: int, db: Session = Depends(get_db)):

    count = (
        db.query(Book)
        .filter(Book.author_id == author_id)
        .count()
    )

    return {
        "author_id": author_id,
        "has_books": count > 0
    }
#--------------------------"Do we have at least one at least one book from a given author---------------------#
@app.get("/stats/categories/{category_id}/has-books")
def category_has_books(category_id: int, db: Session = Depends(get_db)):

    count = (
        db.query(Book)
        .filter(Book.category_id == category_id)
        .count()
    )

    return {
        "category_id": category_id,
        "has_books": count > 0
    }
#-------------Atleast one book in a category----------#
@app.get("/stats/authors/book-count")
def books_per_author(db: Session = Depends(get_db)):

    results = (
        db.query(
            Author.name,
            func.count(Book.id).label("book_count")
        )
        .outerjoin(Book, Book.author_id == Author.id)
        .group_by(Author.id)
        .all()
    )

    return [
        {
            "author_name": name,
            "book_count": count
        }
        for name, count in results
    ]
#-----------no.of books per author-------------#
@app.get("/stats/categories/book-count")
def books_per_category(db: Session = Depends(get_db)):

    results = (
        db.query(
            Category.name,
            func.count(Book.id).label("book_count")
        )
        .outerjoin(Book, Book.category_id == Category.id)
        .group_by(Category.id)
        .all()
    )

    return [
        {
            "category_name": name,
            "book_count": count
        }
        for name, count in results
    ]
#----------No.of books per category--------------#
@app.get("/stats/authors/unique")
def get_unique_authors(db: Session = Depends(get_db)):
    authors = db.query(Author.name).distinct().all()
    return [name for (name,) in authors]
#----------Unique authors list--------------------#
@app.get("/stats/categories/authors")
def get_authors_per_category(db: Session = Depends(get_db)):

    results = (
        db.query(Category.name, Author.name)
        .join(Book, Book.category_id == Category.id)
        .join(Author, Author.id == Book.author_id)
        .distinct()
        .all()
    )

    category_map = {}

    for category_name, author_name in results:
        category_map.setdefault(category_name, []).append(author_name)

    return category_map
#----------Authors per category---------------#
@app.get("/stats/authors/books")
def get_authors_with_books_sorted(db: Session = Depends(get_db)):

    results = (
        db.query(Author.name, Book.title, Book.publication_year)
        .join(Book, Book.author_id == Author.id)
        .order_by(Author.name, Book.publication_year)
        .all()
    )

    author_map = {}

    for author_name, title, year in results:
        author_map.setdefault(author_name, []).append({
            "title": title,
            "publication_year": year
        })

    return author_map

#---------------------Author books sorted by year-------------------------#

models.Base.metadata.create_all(bind=engine)
