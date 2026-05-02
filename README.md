# 🏫 School Web Project

A full-stack web application built with **Django** for managing school tasks and student administration. The platform provides a centralized system for teachers to assign and manage tasks, while students can track their progress through a clean web interface.

---

## 📋 Features

- **Teacher Task Management** — Teachers can create, assign, and manage tasks for students
- **Student Administration Panel** — Admins can manage student records and profiles
- **Task Tracking** — Students can view and interact with assigned tasks
- **Home Dashboard** — A landing page that routes users to the right section of the platform
- **Role-based Navigation** — Separate flows for teachers, students, and admins

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python / Django |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite3 |
| Templating | Django Templates |

---

## 📁 Project Structure

```
School-Web-Project/
├── home/                      # Landing page app
├── tasks/                     # Task model and views
├── studentAdmin/              # Student administration app
├── teacher_task_management/   # Django project settings & URLs
├── templates/                 # Shared HTML templates
├── staticfiles/               # CSS, JS, and static assets
├── manage.py                  # Django management utility
└── db.sqlite3                 # SQLite database
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/moashraf18/School-Web-Project.git
   cd School-Web-Project
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open your browser** and navigate to `http://127.0.0.1:8000/`

---

## ⚙️ Configuration

The Django settings are located in `teacher_task_management/settings.py`. Make sure to update the following before deploying to production:

- `SECRET_KEY` — Replace with a secure, randomly generated key
- `DEBUG` — Set to `False` in production
- `ALLOWED_HOSTS` — Add your domain or server IP

---

## 🗄️ Database

This project uses **SQLite3** by default, which is suitable for development. For production, consider switching to PostgreSQL or MySQL by updating the `DATABASES` setting in `settings.py`.

---

## 📄 License

This project was developed as an academic web development project. Feel free to use it as a reference or starting point for similar school management systems.

---

## 👤 Author

**Mohamed Ashraf**
- GitHub: [@moashraf18](https://github.com/moashraf18)
