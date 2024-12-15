# Book Lending Service API

A RESTful API for a book lending service where registered users can offer books for free and lend books provided by others. Non-registered users can browse available books.

---

## Features:
- **User Authentication**:
  - Register using email and obtain JWT tokens.
- **Book Management**:
  - CRUD operations for books.
  - Filter books by author, genre, condition, and more.
- **Support Resources**:
  - Manage authors, genres, book conditions, and images.
- **Location Information**:
  - Display the location for book pickup.
- **Owner's Decision**:
  - Book owners can decide whom to lend their books to.

---

## Technology Stack:
- **Backend**: Python with Django REST Framework (DRF)
- **Database**: SQLite (default) or PostgreSQL
- **Documentation**: Swagger
- **Containerization**: Docker and Docker Compose
- **Version Control**: Git
- **Unit Testing**: Django's Test Framework

---

## Installation:

### **1. Clone the Repository**
```bash
git clone https://github.com/your_username/book_lending_service.git
cd book_lending_service
