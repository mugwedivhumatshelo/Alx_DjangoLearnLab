# Book API

## Overview
This API provides endpoints for managing books.

## Endpoints
### GET /books/
* List all books

### GET /books/<int:pk>/
* Retrieve a book by ID

### POST /books/create/
* Create a new book

### PUT/PATCH /books/<int:pk>/update/
* Update an existing book

### DELETE /books/<int:pk>/delete/
* Delete a book by ID

## Permissions
* `AllowAny` for GET requests
* `IsAuthenticated` for POST, PUT/PATCH, and DELETE requests

