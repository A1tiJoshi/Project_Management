# Project Management

This is a Django-based project management application that allows users to manage projects, tasks, and team members.

## Features

- User authentication (registration and login)
- CRUD operations for projects, tasks, and team members
- API endpoints for managing projects, tasks, and team members
- Admin interface for managing data

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/Project_Management.git
    cd Project_Management
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Create a [.env](http://_vscodecontentref_/1) file in the root directory and add the following:
      ```properties
      SECRET_KEY=abcd1234
      DEBUG=True
      ALLOWED_HOSTS=localhost,127.0.0.1
      DB_NAME=project_management_db
      DB_USER=project_user
      DB_PASSWORD=securepassword
      DB_HOST=localhost
      DB_PORT=5432
      ```

5. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

6. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ```

7. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

## API Documentation

### Authentication

- **Register**: `POST /auth/register/`
  - Request Body: `{ "username": "...", "password": "..." }`
- **Login**: `POST /auth/login/`
  - Response: `{ "access": "...", "refresh": "..." }`

### Endpoints

- **Projects**
  - `GET /projects/`: List all projects.
  - `POST /projects/`: Create a new project.
  - `GET /projects/<id>/`: Retrieve a project by ID.
  - `PUT /projects/<id>/`: Update a project.
  - `DELETE /projects/<id>/`: Delete a project.

- **Tasks**
  - `GET /tasks/`: List all tasks.
  - `POST /tasks/`: Create a new task.
  - `GET /tasks/<id>/`: Retrieve a task by ID.
  - `PUT /tasks/<id>/`: Update a task.
  - `DELETE /tasks/<id>/`: Delete a task.

- **Team Members**
  - `GET /team-members/`: List all team members.
  - `POST /team-members/`: Create a new team member.
  - `GET /team-members/<id>/`: Retrieve a team member by ID.
  - `PUT /team-members/<id>/`: Update a team member.
  - `DELETE /team-members/<id>/`: Delete a team member.

## Postman Collection

Import the Postman collection `postman_collection.json` from the repository to explore the APIs.

## Running Tests

To run tests, use the following command:
```sh
python manage.py test



