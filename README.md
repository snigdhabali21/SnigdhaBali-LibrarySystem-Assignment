# Library Management System

**Submitted by:** Snigdha Bali  
**Assignment:** FastAPI and React assignment 
**Tech Stack:** FastAPI, SQLAlchemy, SQLite, Python, Postman, SwaggerUI, React-Vite

##  Project Overview

This project is a **Library Management Backend API** built using **FastAPI** and **React-Vite**  
It supports managing **Authors, Categories, and Books**, enforces **authentication using HTTP middleware**, and provides **business insights** through aggregated reports.
All routes are **protected by authentication middleware**.  
The API is designed to be clean, extensible, and easy to test using Postman.
The user friendly interface helps admin to manage the books.

##  Project Structure

```
LibrarySystem/
├── app/
│   ├── __init__.py
│   ├── main.py                # FastAPI app entry point
│   ├── database.py            # Database connection & session
│   ├── models.py              # SQLAlchemy models
│   ├── schemas.py             # Pydantic schemas
│   └── middleware.py          # Authentication
│
├── UI/
│   ├── node_modules/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   │   ├── BookFilters.jsx
│   │   │   ├── BookForm.jsx
│   │   │   └── BookTable.jsx
│   │   ├── pages/
│   │   │   ├── AuthorDetails.jsx
│   │   │   ├── Authors.jsx
│   │   │   ├── Books.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   └── Stats.jsx
│   │   ├── services/
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   ├── .gitignore
│   ├── eslint.config.js
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
├── requirements.txt           # Backend dependencies
└── README.md
```


## Commands to run for Python Project
1. Create a virtual environment and activate-venv\Scripts\activate
2. Install dependencies-pip install -r requirements.txt
3. Run the server- uvicorn app.main:app --port 8001 CRUD output can be checked in **http://127.0.0.1:8000/docs because I have used SwaggerUI**
4. To check the middleware just remove the comments and run the server.
5. Use Postman to check if the authentication is working by entering the credentials.

## Commands to run for Frontend
1. 2 terminals- One for frontend and the other for backend
2. Run the backend with the commands mentioned above.
3. Go to UI using cd command.
4. Run the frontend using the command npm run dev.

## Implementation
CRUD features along with Insights(endpoint) for all the tables are implemented and can be checked in SwaggerUI.



