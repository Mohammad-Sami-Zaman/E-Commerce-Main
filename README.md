# 🛒 E-Commerce Website

A full-stack **E-Commerce Web Application** built with **Python and Django**. The system provides separate functionality for **Admin, Seller, and Customer** users, allowing sellers to manage products and customers to browse and purchase products.

The project is designed with Django's authentication, database models, templates, media handling, and role-based access control.

---

## 🚀 Live Demo

**Live Website:**
https://e-commerce-main-zjq7.onrender.com

---

## 📌 Features

### 👨‍💼 Admin

* Admin authentication
* Manage users
* Manage sellers and customers
* View products
* Manage product categories
* Delete products
* Access Django Admin Panel

### 🏪 Seller

* Seller registration/login
* Add products
* View own products
* Edit own products
* Delete own products
* Upload product images
* View product information
* Manage product listings

### 👤 Customer

* Customer registration/login
* Browse available products
* View product details
* Purchase products
* View product information
* Access customer-specific features

---

## 🛠️ Technologies Used

| Technology               | Purpose              |
| ------------------------ | -------------------- |
| 🐍 Python                | Programming Language |
| 🌐 Django                | Web Framework        |
| 🗄️ SQLite               | Development Database |
| 🖼️ Pillow               | Image Processing     |
| 🎨 HTML5                 | Frontend Structure   |
| 🎨 CSS3                  | Styling              |
| ⚡ Bootstrap              | Responsive UI        |
| 🔐 Django Authentication | User Authentication  |
| 🗂️ Django ORM           | Database Management  |
| 🚀 Render                | Deployment           |
| 📦 Gunicorn              | Production Server    |
| 📁 WhiteNoise            | Static File Serving  |
| 🔧 Git & GitHub          | Version Control      |

---

## 🏗️ Project Structure

```text
E-Commerce-Main/
│
├── manage.py
│
├── Sami_007_product/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── productmanager/
│   ├── migrations/
│   ├── templates/
│   │   ├── master/
│   │   ├── product/
│   │   ├── user/
│   │   └── ...
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── media/
│   └── products/
│
├── db.sqlite3
│
├── requirements.txt
│
└── README.md
```

---

# 👥 User Roles

The application uses three main user roles:

```text
Admin
Seller
Customer
```

### Admin

Has management-level access to the application.

### Seller

Can manage products that belong to the seller.

### Customer

Can browse products and purchase products.

---

# 🔐 Authentication

The project uses Django's authentication system.

Users can:

* Register
* Login
* Logout
* Access role-specific functionality
* Manage their account

A custom user model is used for role management.

Example:

```python
class CustomUserModel(AbstractUser):

    role_type = [
        ('Admin', 'Admin'),
        ('Seller', 'Seller'),
        ('Customer', 'Customer'),
    ]

    role = models.CharField(
        choices=role_type,
        null=True
    )
```

---

# 📦 Product Management

Sellers can create and manage their products.

A product contains information such as:

* Product name
* Product image
* Category
* Price
* Seller
* Description
* Creation date

Example product image field:

```python
product_image = models.ImageField(
    upload_to='products/',
    null=True,
    blank=True
)
```

---

# 🖼️ Media & Product Images

Uploaded product images are stored using Django's media configuration.

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Images are displayed in templates using:

```django
{% if product.product_image %}
    <img src="{{ product.product_image.url }}"
         alt="{{ product.product_name }}">
{% endif %}
```

---

# 🎨 Static Files

The project uses Django static files for CSS, JavaScript, and static images.

```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

WhiteNoise is used to serve static files in production.

---

# 🛡️ CSRF Protection

Django's built-in CSRF protection is enabled for POST requests.

Forms use:

```django
<form method="POST">
    {% csrf_token %}
```

The Render production domain is configured through:

```python
CSRF_TRUSTED_ORIGINS = [
    'https://e-commerce-main-zjq7.onrender.com',
]
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Mohammad-Sami-Zaman/E-Commerce-Main.git
```

Go into the project:

```bash
cd E-Commerce-Main
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv myEnv
```

Activate it:

```bash
myEnv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv myEnv
```

Activate:

```bash
source myEnv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Apply Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

## 5. Create Superuser

```bash
python manage.py createsuperuser
```

Enter:

```text
Username
Email
Password
```

---

## 6. Collect Static Files

```bash
python manage.py collectstatic
```

---

## 7. Run the Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

# 📋 Requirements

Example `requirements.txt`:

```text
Django==6.0.7
Pillow==12.3.0
asgiref==3.12.1
sqlparse==0.5.5
tzdata==2026.3
gunicorn
whitenoise
```

---

# 🚀 Deployment on Render

The application is deployed using **Render**.

### Build Command

```bash
pip install -r requirements.txt && python manage.py collectstatic --no-input
```

### Start Command

```bash
gunicorn Sami_007_product.wsgi:application
```

### Environment Variables

For production, configure:

```text
SECRET_KEY=your-secret-key
DEBUG=False
```

The Render hostname is handled through:

```python
RENDER_EXTERNAL_HOSTNAME = os.environ.get(
    'RENDER_EXTERNAL_HOSTNAME'
)
```

---

# 🔒 Security

For production deployment:

* `DEBUG=False`
* Use environment variables for `SECRET_KEY`
* Configure `ALLOWED_HOSTS`
* Configure `CSRF_TRUSTED_ORIGINS`
* Keep Django CSRF protection enabled
* Do not expose sensitive credentials
* Use a production database
* Use persistent storage for uploaded media

---

# 🗄️ Database

The project uses SQLite during development:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

For a production e-commerce application, PostgreSQL is recommended.

---

# 🔄 Application Workflow

```text
                E-Commerce Website
                       │
          ┌────────────┴────────────┐
          │                         │
       Authentication          Product System
          │                         │
    ┌─────┼─────┐             ┌─────┼─────┐
    │     │     │             │     │     │
  Admin Seller Customer      Add   Edit  Delete
    │     │     │             │     │     │
    └─────┴─────┘             └─────┴─────┘
          │
          ▼
     Role-Based Access
```

---

# 📸 Product Management Workflow

```text
Seller Login
     │
     ▼
Product Dashboard
     │
     ├── Add Product
     │      │
     │      ▼
     │   Upload Image
     │      │
     │      ▼
     │   Save Product
     │
     ├── Edit Product
     │
     └── Delete Product
```

---

# 🧑‍💻 Developer

**Mohammad Sami Zaman**

Computer Science & Engineering

### Skills Used

* Python
* Django
* HTML
* CSS
* Bootstrap
* SQLite
* Git
* GitHub
* Render

---

# 📂 Repository

GitHub Repository:

https://github.com/Mohammad-Sami-Zaman/E-Commerce-Main

---

# 📜 License

This project is developed for educational and portfolio purposes.

You are free to study and modify the project for learning purposes.

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 🎯 Future Improvements

Possible future improvements include:

* 🛒 Shopping cart
* 💳 Online payment integration
* 📦 Order tracking
* ⭐ Product reviews and ratings
* 🔍 Advanced product search
* 🏷️ Product discounts
* ❤️ Wishlist
* 📊 Seller dashboard
* 📈 Sales analytics
* 🗄️ PostgreSQL production database
* ☁️ Cloudinary/AWS S3 image storage
* 📧 Email notifications
* 📱 Improved mobile responsiveness
* 🔐 Enhanced security and permissions
