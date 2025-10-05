### API Endpoints Overview

| Method | Endpoint | Description | Authentication |
|--------|-----------|--------------|----------------|
| GET | `/api/books/` | Retrieve all books | No |
| GET | `/api/books/<id>/` | Retrieve a single book | No |
| POST | `/api/books/create/` | Create a new book | Yes |
| PUT/PATCH | `/api/books/<id>/update/` | Update an existing book | Yes |
| DELETE | `/api/books/<id>/delete/` | Delete a book | Yes |

#### Permissions
- Authenticated users can Create, Update, and Delete.
- Unauthenticated users can only Read (List and Detail).
