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
- protected /users/me endpoint

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