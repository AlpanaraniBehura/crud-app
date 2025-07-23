# Django CRUD App

A simple Django-based web application for managing employee records using CRUD (Create, Read, Update, Delete) operations.

## 🚀 Features

- Add new employee records
- View a list of employees
- Edit existing employee details
- Delete employee records
- Fully functional web interface


---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap (optional)
- **Database:** SQLite (default Django DB)

---

## 📂 Project Structure

crud-app/
│
├── core/
│ ├── migrations/
│ ├── templates/core/
│ │ ├── add.html
│ │ ├── edit.html
│ │ ├── delete.html
│ │ └── list.html
│ ├── admin.py
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── urls.py
│ └── ...
│
├── db.sqlite3
├── manage.py
└── README.md


---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/AlpanaraniBehura/crud-app.git
cd CRUD
2. Create a virtual environment (optional but recommended)
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate

3. Install dependencies
pip install django

4. Run migrations
python manage.py migrate

5.Create a superuser (for accessing the admin panel):
python manage.py createsuperuser

6. Start the development server
python manage.py runserver

7. Visit in browser
http://127.0.0.1:8000/

8.REST API Integration
This CRUD app now also supports full REST API functionality using Django REST Framework (DRF).

📁 API Endpoints
Method	    Endpoint	          Description
GET 	/api/employees/ 	    List all employees
POST	/api/employees/	        Create a new employee
GET	    /api/employees/{id}/	Retrieve employee by ID
PUT 	/api/employees/{id}/	Update employee by ID
DELETE  /api/employees/{id}/	Delete employee by ID

🔧 How to Use the API
You can test API endpoints using:
1)Postman
2)cURL
3)Your browser (for GET requests)

Example POST Request (JSON Body):
{
  "name": "Robert",
  "email": "robert@example.com",
  "position": "Backend Developer"
}
Example PUT Request:
Update existing employee (e.g. /api/employees/1/):

{
  "name": "Updated Name",
  "email": "updated@example.com",
  "position": "Fullstack Developer"
}

⚙️ Tools & Technologies Used
1)Django 5.1.3
2)Django REST Framework
3)HTML5, CSS3 for frontend

✍️
Alpana Rani Behura
GitHub: @AlpanaraniBehura