from pydantic import BaseModel
from typing import Optional, List

class AuthorBase(BaseModel):#Used for common fields
    name: str
    bio: Optional[str] = None #Field is allowed to be NULL


class AuthorCreate(AuthorBase):
    pass #it has inherited from Base and intentionally left empty to maintain schema


class AuthorResponse(AuthorBase):
    id: int

    class Config:
        from_attributes = True #FASTApi converts the obj to JSON automatically

class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True

class BookBase(BaseModel):
    title: str
    isbn: Optional[str] = None
    publication_year: Optional[int] = None
    author_id: int
    category_id: int


class BookCreate(BookBase):
    pass


class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True
