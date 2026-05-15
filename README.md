# Auth-Serice

A production-ready authentication microservice built with FASTAPI, PostgreSQL, JWT, and Docker.

## Overview

This project provides a complete authentication backend that supports:
- User registration
- User login
- Password hashing using bcrypt
- JWT access token generation
- Protected user profile endpoint
- PostgreSQL database integration
- Docker-based containerization

The goal was to build a backend service using clean architecture and modern development practices

## Features 

### Authentication

- User signup
- User login
- password hashing with bcrypt
- JWT token generation
- protected `/users/me` endpoint

### Database

- PostgreSQL
- SQLALchemy ORM

### API

- Request validation using pydantic
- Automatic Swagger documentation
- Proper HTTP status codes

### Devops

- Dockerized application
- Docker Compose for app + database

## Tech Stack

### Backend 

- Python 3.10
- FastAPI
- Uvicorn

### Database

- PostgreSQL
- SQLALchemy

### Devops

- Docker 
- Docker Compose 

## Project Structure

```
auth-service/
├── app/ 
│ ├── main.py 
│ ├── auth/ │ 
│ └── auth.py 
│ ├── db/ 
│ │ └── db.py 
│ ├── models/ 
│ │ └── users_model.py 
│ ├── schemas/ 
│ │ └── user_schema.py 
│ ├── routers/ 
│ │ └── users.py 
│ └── services/ 
├── Dockerfile 
├── docker-compose.yml 
├── requirements.txt 
├── README.md 
└── .env
```

## API Endpoints

### Authentication Endpoints

|Method|Endpoint|Description|
|----|----------------|-----------------------------|
|POST|`/users/me`|Registers a new user|
|POST|`/users/login`|Login and recieve a JWT token|
|POST|`/users/me`|Get current authenticated user|

## Local Development Setup

1. #### Clone the Repository 

```
git clone https://github.com/vanika02/auth-service.git
cd auth-service
```

2. #### Create virtual environment 

```
python3 -m venv venv
source venv/bin/activate
```

3. #### Install Dependencies

```
pip install -r requirements.txt
```

4. #### Configure PostgreSQL

create a PostgrSQL database and update the database URL.

5. #### Run the application

```
uvicorn app.main:app --reload
```

6. #### Open swagger documentation 
```
http://localhost:8000/docs
```

### Running with Docker 

#### Build and start containers 

```
docker compose up --build
```

#### Access the API
```
http://localhost:8000/docs
```

### Example API Usage

#### Signup

```
curl -X POST http://localhost:8000/users/signup \
-H "Content-Type: application/json" \
-d '{
  "username": "vanika",
  "email": "vanika@example.com",
  "password": "securepassword123"
}'
```

### Login 
```
curl -X POST http://localhost:8000/users/login \
-H "Content-Type: application/json" \
-d '{
    "email": "vanika@example.com",
    "password": "securepassword123"
}'
```

### Get Current User 
```
curl -X GET http://localhost:8000/users/me \
-H "Authorization: Bearer <access_token>"
```

### Authentication Flow

client<br>
&darr;<br>
signup/login Request<br>
&darr;<br>
FastAPI Router<br>
&darr;<br>
Schema Validation<br>
&darr;<br>
Database query<br>
&darr;<br>
password hashing / verfication<br>
&darr;<br>
JWT token generation<br> 
&darr;<br>
JSON response<br>

### Deployment 

This project can be deployed using Docker on cloud platforms such as:
- Render
- Railway
- Fly.io

After deployment, Swagger documentation is available at:
```
https://your-service-url.onrender.com/docs
```

### Future Improvements

- Refresh tokens 
- Role-based access control
- Email verification
- Password reset
- Unit and integration tests
- CI/CD pipeline

### Key Learninga 

This project helped me gain hands-on experience with:

- REST API developement
- Authentication and authorization
- JWT tokens 
- password hashing 
- SQLAlchemy ORM
- PostgreSQL
- Docker and containerization
- clean backend architecture

