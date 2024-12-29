
---

## **Project Management System Backend**
A backend system built with Django and PostgreSQL to manage projects, tasks, and team members. It includes CRUD APIs, JWT authentication, Redis caching, and Celery for background task management.

---

### **Features**
- Project, Task, and Team Member management.
- JWT authentication for secure access.
- Redis caching for performance optimization.
- Background tasks handled by Celery.
- Admin interface for easy management.

---

### **Technologies Used**
- Python (Django Framework)
- PostgreSQL
- Django REST Framework (DRF)
- Celery with Redis
- Docker (optional)

---

### **Setup Instructions**

#### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/project-management-system.git
cd project-management-system
```

#### **2. Create and Activate a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

#### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

#### **4. Set Up the PostgreSQL Database**
1. Install PostgreSQL.
2. Create a new database:
   ```sql
   CREATE DATABASE project_management;
   ```
3. Update `DATABASES` in `settings.py` with your database credentials.

#### **5. Apply Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

#### **6. Run the Development Server**
```bash
python manage.py runserver
```

The server will be available at `http://127.0.0.1:8000`.

---

### **API Documentation**

#### **Authentication**
- **Register**: `POST /auth/register/`
  - Request Body: `{ "username": "...", "password": "..." }`
- **Login**: `POST /auth/login/`
  - Response: `{ "access": "...", "refresh": "..." }`

#### **Endpoints**
- **Projects**
  - `GET /projects/`: List all projects.
  - `POST /projects/`: Create a new project.
  - `GET /projects/<id>/`: Retrieve a project by ID.
  - `PUT /projects/<id>/`: Update a project.
  - `DELETE /projects/<id>/`: Delete a project.
- **Tasks**
  - `GET /tasks/`: List all tasks.
  - CRUD operations similar to projects.
- **Team Members**
  - CRUD operations similar to projects.

Import the Postman collection `postman_collection.json` from the repository to explore the APIs.

---

### **Background Tasks with Celery**

#### **1. Install Redis**
On Linux:
```bash
sudo apt update
sudo apt install redis
```
On macOS:
```bash
brew install redis
```

#### **2. Start Redis Server**
```bash
redis-server
```

#### **3. Run Celery Worker**
```bash
celery -A project_management_system worker --loglevel=info
```

#### **4. Example Background Task**
The `send_email_task` function in `tasks.py` is an example background task. It can be triggered programmatically.

---

### **Optimizations**
- Use `select_related` and `prefetch_related` in queries to reduce database hits.
- Redis caching implemented for frequently queried data.

---

### **Admin Interface**
Access the admin panel at `http://127.0.0.1:8000/admin`. Use the superuser credentials created during setup.

---

### **Testing**
Run tests with:
```bash
python manage.py test
```

---

### **License**
This project is licensed under the MIT License.

---

