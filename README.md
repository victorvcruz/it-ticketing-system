# IT Ticketing System

A ticket management system for IT support, built with Python, FastAPI, SQLAlchemy (async), PostgreSQL, and Alembic.

## Overview

This project provides an API for managing IT support tickets, allowing user registration, ticket creation, status updates, and assignment of technicians.

### Main Features

- User registration and listing (admin, technician, employee)
- Ticket creation, listing, and status updates
- Filtering tickets by status
- Relationship between users and tickets (requester and technician)
- User authentication (password hashing)
- Database migrations with Alembic

## Project Structure

```
it-ticketing-system/
├── alembic/                # Database migrations
├── src/
│   └── it_ticketing_system/
│       ├── controllers/    # FastAPI routes (users, tickets)
│       ├── dao/            # Data Access Objects (UserDAO, TicketDAO)
│       ├── models/         # ORM models (User, Ticket)
│       ├── schemas/        # Pydantic schemas (validation and serialization)
│       ├── db.py           # Async database configuration
│       ├── config.py       # Environment variable loading
│       └── main.py         # FastAPI application entry point
├── docker-compose.yml      # PostgreSQL service for development
├── pyproject.toml          # Project dependencies (Poetry)
└── README.md               # This file
```

## How to Run Locally

### 1. Prerequisites

- Python 3.11+
- [Poetry](https://python-poetry.org/)
- Docker and Docker Compose

### 2. Clone the repository

```bash
git clone https://github.com/your-username/it-ticketing-system.git
cd it-ticketing-system
```

### 3. Start PostgreSQL with Docker

```bash
docker-compose up -d
```

The database will be available at `localhost:5432` with user and password `postgres`.

### 4. Configure environment variables

Create a `.env` file in the project root with:

```
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/it_ticketing_system
```

### 5. Install dependencies

```bash
poetry install
```

### 6. Apply database migrations

```bash
poetry run alembic upgrade head
```

### 7. Run the application

```bash
poetry run uvicorn src.it_ticketing_system.main:app --reload
```

The API will be available at [http://localhost:8000](http://localhost:8000).

## API Documentation

Interactive documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs).