# To-Do List API

A simple Flask-based REST API for managing a to-do list, generated from a Swagger specification. This project demonstrates how to create and manage a to-do list using a structured API.

---

## Features

- **View All To-Dos**: Retrieve a list of all to-do items.
- **Create a New To-Do**: Add a new to-do item with a title, description, and completion status.
- **View a Specific To-Do**: Retrieve details of a to-do item by its ID.
- **Update a To-Do**: Modify an existing to-do item by its ID.
- **Delete a To-Do**: Remove a to-do item by its ID.

---

## API Specification

The API is defined using the Swagger (OpenAPI 2.0) specification. View the Swagger UI at:
[http://localhost:5000/api/docs](http://localhost:5000/api/docs)

### Endpoints

| Endpoint         | Method | Description                         |
|------------------|--------|-------------------------------------|
| `/todos`         | GET    | Retrieve a list of all to-do items. |
| `/todos`         | POST   | Create a new to-do item.            |
| `/todos/{id}`    | GET    | Retrieve details of a specific to-do item. |
| `/todos/{id}`    | PUT    | Update a specific to-do item.       |
| `/todos/{id}`    | DELETE | Delete a specific to-do item.       |

---

## Prerequisites

- **Python 3.7+**
- **Pip** (Python package manager)
- Install project dependencies from the `requirements.txt` file.

---

## Setup Instructions

1. **Clone the repository**:
   ```bash
   [git clone https://github.com/your-username/todo-api.git](https://github.com/cyd0c/Swagger_Flask.git)


2. **run app.py   

3. **navigate to
  ```
   http://localhost:5000/api/docs
```


5.*** test the api endpoint on swagger ui
