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


## Folder Structure

```
auth-service/
├── app/
│   ├── main.py
│   ├── routers/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── db/
├── Dockerfile
├── requirements.txt
└── README.md
```