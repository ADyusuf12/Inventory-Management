# Inventory-Management
A Django REST Framework-powered inventory management API
📌 Overview
The Inventory Management System is a RESTful API built with Django REST Framework (DRF). It allows users to perform CRUD operations on product inventory while ensuring secure authentication, data validation, and efficient pagination.
🚀 Features
✅ CRUD Operations – Create, Retrieve, Update, and Delete products
✅ Authentication – JWT-based authentication for secure API access
✅ Input Validation – Enforces business rules for data integrity
✅ Pagination – Efficient handling of large datasets
✅ Unit Testing – Automated tests for reliability and robustness
🔧 Tech Stack
- Backend: Python, Django REST Framework
- Database: SQLite (can be replaced with PostgreSQL/MySQL)
- Authentication: JWT (Django REST Framework Simple JWT)
- Testing: Django TestCase, DRF APIClient
- API Documentation: Postman

🛠️ Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/ADyusuf12/inventory-management.git
cd inventory-management


2️⃣ Create & Activate Virtual Environment
python -m venv env
source env/bin/activate  # macOS/Linux
env\Scripts\activate  # Windows


3️⃣ Install Dependencies
pip install -r requirements.txt


4️⃣ Apply Migrations
python manage.py migrate


5️⃣ Run the Development Server
python manage.py runserver


The API is now accessible at: http://127.0.0.1:8000/
🔑 Authentication
Obtain a JWT Token
Send a POST request to /api/token/ with valid credentials:
{
    "username": "your_username",
    "password": "your_password"
}


This returns:
{
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}


Use the access_token in API requests:
Authorization: Bearer your_access_token


📦 API Endpoints
| Method | Endpoint | Description | 
| POST | /api/token/ | Obtain JWT token | 
| POST | /api/token/refresh/ | Refresh expired token | 
| GET | /api/products/ | List all products (paginated) | 
| POST | /api/products/ | Create a new product | 
| GET | /api/products/{id}/ | Retrieve a single product | 
| PUT | /api/products/{id}/ | Update a product | 
| DELETE | /api/products/{id}/ | Delete a product | 


🔍 Testing
Run unit tests using:
python manage.py test inventory


This validates: ✔ CRUD operations
✔ Authentication
✔ Validation rules
✔ Edge cases

📖 Future Enhancements
🚀 Search & Filtering – Implement search functionality for products
🚀 Category Management – Allow products to be categorized
🚀 Admin Panel Improvements – Enhance user roles & permissions

🤝 Contributing
Contributions are welcome! If you’d like to improve this project:
- Fork the repo & create a new branch (feature-branch)
- Make your updates & commit
- Open a Pull Request

📧 Contact
For inquiries, contact me via: 📩 Email: adyusuf68@gmail.com
📌 GitHub: ADyusuf12
