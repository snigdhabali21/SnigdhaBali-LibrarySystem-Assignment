# Library Management API

**Submitted by:** Snigdha Bali  
**Assignment:** FastAPI Intern Assignment  
**Tech Stack:** FastAPI, SQLAlchemy, SQLite, Python, Postman, SwaggerUI 

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
├── .gitignore # Ignored files
├── requirements.txt # Dependencies
## 📂 Project Structure

```
LibrarySystem/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── middleware.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```


## Commands to run
1.Create a virtual environment and activate-venv\Scripts\activate
2.Install dependencies-pip install -r requirements.txt
3.Run the server- uvicorn app.main:app --port 8001
**http://127.0.0.1:8000/docs because I have used SwaggerUI**
4.To check the middleware just remove the comments and run the server.
5.Use Postman to check if the authentication is working by entering the credentials.

## Implementation
CRUD features along with Insights(endpoint) for all the tables are implemented and can be checked in SwaggerUI.



