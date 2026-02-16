from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

class Author(Base):
    __tablename__ = "authors"  #tells SQLite to create a table Authors

    id = Column(Integer, primary_key=True, index=True)#Indexing helps to search fast.NOt required to use index everywhere..Just for the PK n FK as we use them frequently
    name = Column(String, nullable=False)#nullable means cannot be empty
    bio = Column(String, nullable=True)

    books = relationship("Book", back_populates="author")  #This means author and books tables are connected i.e, JOIN

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)

    books = relationship("Book", back_populates="category")

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    isbn = Column(String, nullable=True)
    publication_year = Column(Integer, nullable=True)

    author_id = Column(Integer, ForeignKey("authors.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))

    author = relationship("Author", back_populates="books")
    category = relationship("Category", back_populates="books")
