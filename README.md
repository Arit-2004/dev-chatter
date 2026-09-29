# 🚀 DevChatter

**DevChatter** is a Twitter-inspired social media web application built with **Python and Django**. Users can create, edit, delete, and search tweets, along with uploading images.

The project is designed with a responsive interface that works across **desktop and mobile devices**.

## 🌐 Live Demo

**Live Application:**
https://myproject-yyop.vercel.app/

---

## ✨ Features

* 🔐 User Registration & Login
* 📝 Create Tweets
* ✏️ Edit Tweets
* 🗑️ Delete Tweets
* 🖼️ Upload Images with Tweets
* 🔎 Search Tweets
* 👤 Display Tweets by Username
* 📱 Responsive Mobile & Desktop UI
* 🗄️ PostgreSQL Database
* ☁️ Cloudinary Image Storage
* 🚀 Deployed on Vercel

---

## 🛠️ Tech Stack

| Technology       | Purpose                |
| ---------------- | ---------------------- |
| **Python**       | Programming Language   |
| **Django**       | Web Framework          |
| **PostgreSQL**   | Database               |
| **Bootstrap 5**  | UI & Responsive Design |
| **Cloudinary**   | Image Storage          |
| **Vercel**       | Deployment             |
| **Git & GitHub** | Version Control        |

---

## 📂 Project Structure

```text
dev-chatter/
│
└── myproject/
    │
    ├── manage.py
    ├── requirements.txt
    │
    ├── chai/
    │   ├── migrations/
    │   ├── templates/
    │   ├── models.py
    │   ├── views.py
    │   ├── forms.py
    │   ├── urls.py
    │   └── admin.py
    │
    ├── myproject/
    │   ├── settings.py
    │   ├── urls.py
    │   ├── views.py
    │   ├── wsgi.py
    │   └── asgi.py
    │
    ├── static/
    └── templates/
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Arit-2004/dev-chatter.git
```

### 2. Navigate to the project

```bash
cd dev-chatter/myproject
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file inside the `myproject` directory:

```env
DJANGO_SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=your_database_port

CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

> ⚠️ Never upload your `.env` file or expose your secret keys publicly.

---

## 🗄️ Database Setup

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

---

## ▶️ Run the Project

Start the Django development server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 🔑 Authentication

DevChatter uses Django's built-in authentication system for:

* User registration
* Login
* Logout
* Session management

Authentication URLs are handled through Django's authentication system.

---

## 🖼️ Image Uploads

Tweet images are stored using **Cloudinary** instead of the local filesystem.

This makes image uploads suitable for deployment environments such as Vercel, where the local filesystem is not persistent.

---

## 🔍 Search

Users can search tweets using the search bar.

The application searches tweet content using Django's:

```python
icontains
```

lookup.

---

## 📱 Responsive Design

The interface is built using **Bootstrap 5** and custom CSS.

The application supports:

* Desktop screens
* Tablets
* Mobile phones
* Responsive navigation
* Mobile-friendly tweet forms

---

## 🚀 Deployment

The application is deployed using:

* **Vercel** → Application hosting
* **PostgreSQL** → Database
* **Cloudinary** → Image storage

Production environment variables are configured through the Vercel dashboard.

---

## 🎯 What I Learned

While building DevChatter, I gained practical experience with:

* Django project structure
* Django models and ORM
* CRUD operations
* Forms and file uploads
* User authentication
* PostgreSQL integration
* Cloudinary integration
* Responsive UI development
* Environment variables
* Git & GitHub
* Vercel deployment
* Debugging production issues

---

## 🔮 Future Improvements

Some features I may add in the future:

* ❤️ Like and unlike tweets
* 💬 Comments
* 👤 User profiles
* 🔔 Notifications
* 🌙 Improved theme customization
* 📄 Pagination
* 🔐 Additional security improvements

---

## 👨‍💻 Author

**Aritra Mahattam**

GitHub:
https://github.com/Arit-2004

---

## ⭐ Support

If you find this project interesting, consider giving the repository a ⭐ on GitHub!

---

**Built with Python & Django ❤️**
