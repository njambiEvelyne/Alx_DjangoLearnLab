# Django REST Framework - Book API

## Overview
This API provides CRUD operations for managing books using Django REST Framework (DRF).
- Supports listing, retrieving, creating, updating, and deleting books.
- Implements authentication-based access control.

## Endpoints and Views

| HTTP Method | Endpoint         | View Used          | Description |
|------------|-----------------|--------------------|-------------|
| GET        | /api/books/      | `BookListView`    | Retrieve all books (public) |
| GET        | /api/books/<int:pk>/ | `BookDetailView`  | Retrieve details of a book (public) |
| POST       | /api/books/create/ | `BookCreateView` | Create a new book (authenticated users only) |
| PUT/PATCH  | /api/books/update/<int:pk>/ | `BookUpdateView` | Update a book (authenticated users only) |
| DELETE     | /api/books/delete/<int:pk>/ | `BookDeleteView` | Delete a book (authenticated users only) |

## Authentication
- **Public Access**: `GET` requests (ListView & DetailView) do not require authentication.
- **Protected Access**: `POST`, `PUT/PATCH`, and `DELETE` requests require user authentication.

## Permissions Used
- `permissions.AllowAny`: Grants public access to ListView and DetailView.
- `permissions.IsAuthenticated`: Requires users to be logged in for Create, Update, and Delete actions.

## Custom Features
- **Duplicate Prevention**: The `perform_create` method in `BookCreateView` ensures that books with duplicate titles cannot be added.
- **Security**: Authenticated users are required for write operations.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/advanced_api_project.git
   cd advanced_api_project

##  Enhanced Query Features

###  Filtering
You can filter books using query parameters:
- `title`: Filter books by title  
- `author`: Filter books by author  
- `publication_year`: Filter books by publication year  

**Example Usage:**  
```bash
GET /api/books/?title=The Great Gatsby
GET /api/books/?author=J.K. Rowling
GET /api/books/?publication_year=2023


##  API Testing Strategy

###  Running Tests
Run all API tests using:
```bash
python manage.py test api