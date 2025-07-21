# Django CRUD App

A simple Django-based web application for managing employee records using CRUD (Create, Read, Update, Delete) operations.

## 🚀 Features

- Add new employee records
- View a list of employees
- Edit existing employee details
- Delete employee records
- Fully functional web interface

## 📸 Screenshots

| Add Employee | Employee List | Edit Employee |
|--------------|---------------|---------------|
| ![Add](screenshots/add.png) | ![List](screenshots/list.png) | ![Edit](screenshots/edit.png) |

> _Note: Add your screenshots in a `screenshots` folder or remove this section._

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

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/AlpanaraniBehura/crud-app.git
cd crud-app
2. Create a virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install django
4. Run migrations
bash
Copy
Edit
python manage.py migrate
5. Start the development server
bash
Copy
Edit
python manage.py runserver
6. Visit in browser
cpp
Copy
Edit
http://127.0.0.1:8000/
✍️ Author
Alpana Rani Behura

GitHub: @AlpanaraniBehura