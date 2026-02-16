# Library Management API

**Submitted by:** Snigdha Bali  
**Assignment:** FastAPI Intern Assignment  
**Tech Stack:** FastAPI, SQLAlchemy, SQLite, Python, Postman 

##  Project Overview

This project is a **Library Management Backend API** built using **FastAPI**.  
It supports managing **Authors, Categories, and Books**, enforces **authentication using HTTP middleware**, and provides **business insights** through aggregated reports.
All routes are **protected by authentication middleware**.  
The API is designed to be clean, extensible, and easy to test using Postman.

##  Project Structure
LibrarySystem/
├── app/
│ ├── main.py # FastAPI app entry point
│ ├── database.py # Database connection & session
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── middleware.py # Authentication 
│ └── init.py
│
├── .env # Login credentials
├── .gitignore # Ignored files
├── requirements.txt # Dependencies

## Commands to run
1.Create a virtual environment and activate-venv\Scripts\activate
2.Install dependencies-pip install -r requirements.txt
3.

