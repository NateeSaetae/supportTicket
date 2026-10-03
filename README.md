# AI Support Ticket System

A RESTful API for managing customer support tickets, built with **Python, FastAPI, and PostgreSQL**.

This project focuses on backend development, database design, REST API best practices, and maintainable software architecture. It is designed to support future AI integration for automated ticket classification, prioritization, and summarization.

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Database:** PostgreSQL (planned)
- **ORM:** SQLAlchemy (planned)
- **Testing:** Pytest
- **API Documentation:** Swagger UI

## Features

### Implemented
- FastAPI project initialization
- Health Check API
- Interactive API documentation using Swagger UI

### Planned
- Create, retrieve, and update support tickets
- Ticket status management
- Soft Delete
- Filter tickets by status
- Pagination
- PostgreSQL integration
- Automated API testing
- AI-powered ticket classification and summarization (future enhancement)

## Project Structure

```text
supportTicket/
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
├── .gitignore
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/NateeSaetae/supportTicket.git
cd supportTicket
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the virtual environment.

**Windows (CMD):**
```cmd
.venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Application

```bash
python -m uvicorn app.main:app --reload
```

The application will be available at:

http://127.0.0.1:8000

## API Documentation

FastAPI automatically generates interactive API documentation.

**Swagger UI:** http://127.0.0.1:8000/docs

## Available Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Check application health |

Additional endpoints will be implemented during development.

## Future AI Integration

The system is designed to support AI-powered features such as:

- Automatic ticket categorization
- Priority prediction
- Ticket summarization

AI integration is planned for a future development phase and is not included in the initial version.

## Project Status

**In Development**

Current phase: Backend initialization and database design.