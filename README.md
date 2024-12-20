# Book Lending Service API

A RESTful API for a book lending service where registered users can offer books for free, lend books provided by others, and manage requests to borrow books. Non-registered users can browse available books.

---

## Features:
- **User Authentication**:
  - Register using email and obtain JWT tokens.
  - Users can create an account with full name, email, username, and mobile number.
  - Password validation and confirmation during registration.

- **User Management**:
  - View and update user details.
  - CRUD operations for user profiles.

- **Book Management**:
  - CRUD operations for books.
  - Filter books by author, genre, condition, and more.
  - Book owners can manage lending requests and decide who gets to borrow their books.

- **Request Management**:
  - Registered users can send book lending requests.
  - Book owners can accept or reject lending requests.

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
- **User Authentication**: JWT (JSON Web Tokens)
- **API Documentation**: Swagger (drf-yasg)
- **Containerization**: Docker and Docker Compose
- **Version Control**: Git
- **Unit Testing**: Django's Test Framework

---

## Installation:

### **1. Clone the Repository**
```bash
git clone https://github.com/your_username/book_lending_service.git
cd book_lending_service
