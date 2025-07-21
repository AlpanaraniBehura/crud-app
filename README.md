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

CRUD/
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

✍️
Alpana Rani Behura
GitHub: @AlpanaraniBehura