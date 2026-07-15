# Task Manager API with JWT Authentication

## Overview

This project is a RESTful Task Manager API built using FastAPI. It supports user authentication using JWT tokens and allows authenticated users to manage their own tasks securely.

## Features

* User Registration
* User Login using JWT Authentication
* Password Hashing using Passlib (bcrypt)
* Protected API Endpoints
* User-specific Task Management
* SQLite Database
* SQLAlchemy ORM
* Interactive Swagger Documentation

## Technologies Used

* FastAPI
* Python
* SQLite
* SQLAlchemy
* Pydantic
* JWT (python-jose)
* Passlib (bcrypt)

## Project Structure

```
TaskManagerAPI/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── security.py
├── dependencies.py
├── auth.py
├── tasks.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository

```
git clone <repository-url>
```

2. Create a virtual environment

```
python3 -m venv venv
```

3. Activate the virtual environment

macOS/Linux

```
source venv/bin/activate
```

Windows

```
venv\Scripts\activate
```

4. Install dependencies

```
pip install -r requirements.txt
```

5. Run the application

```
uvicorn main:app --reload
```

## API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

## Authentication Endpoints

* POST /auth/signup
* POST /auth/login
* GET /auth/me

## Task Endpoints

* POST /tasks
* GET /tasks
* GET /tasks/{id}
* PUT /tasks/{id}
* DELETE /tasks/{id}

## Authentication Flow

1. Register a new user.
2. Login using email and password.
3. Copy the generated JWT access token.
4. Click **Authorize** in Swagger.
5. Access protected task endpoints.

## Author

Uday Kiran
