# To-Do-List
A backend-only To-Do List application built with Django REST Framework (DRF) that implements JWT authentication for secure user access. The API allows users to register, log in, and manage their personal tasks (CRUD operations). All endpoints are tested and verified in Postman.


## Features:
- User registration and login using JWT (JSON Web Tokens)
- Secure authentication with Django REST Framework
- CRUD operations for user-specific To-Do tasks
- Validation and error handling with DRF serializers
- Tested thoroughly using Postman

## Tech Stack:
- Backend: Django, Django REST Framework
- Authentication: JWT (SimpleJWT)
- Database: MySQL (or SQLite, depending on your setup)
- Testing Tool: Postman

## How to Run
1. Clone the repository
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Run the server: `python manage.py runserver`