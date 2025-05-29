This is a Notes Taking API project built using Django and Django REST Framework. The project allows users to register and log in using JWT (JSON Web Token) authentication. Once authenticated, users can perform CRUD operations on their personal notes. CRUD stands for Create, Read, Update, and Delete. The API is protected so that only logged-in users can access their own notes.

The backend uses SQLite as the database by default, and all requests are made using endpoints such as /api/register/ for user registration, /api/login/ for JWT token login, and /api/notes/ for managing notes. To access these endpoints, users must include a valid JWT access token in the Authorization header using the format: Bearer followed by the token.

This project is a beginner-friendly implementation designed to help new developers understand how to use Django REST Framework to create APIs with user authentication and secure access. The application includes everything needed to build a fully functional note management backend with user-based access and authentication.

