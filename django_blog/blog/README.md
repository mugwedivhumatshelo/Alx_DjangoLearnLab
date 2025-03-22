Authentication System Documentation
Overview
The authentication system is a critical component of the Django blog project. It provides a secure way for users to register, log in, and manage their profiles.

Registration
- URL: /register/
- Method: POST
- Fields:
    - username
    - email
    - password1
    - password2
- Description: Creates a new user account.

Login
- URL: /login/
- Method: POST
- Fields:
    - username
    - password
- Description: Authenticates a user and logs them in.

Logout
- URL: /logout/
- Method: GET
- Description: Logs a user out.

Profile
- URL: /profile/
- Method: GET, POST
- Fields:
    - email
- Description: Displays and updates a user's profile information.

Security Measures
- CSRF Protection: Implemented using Django's built-in CSRF protection.
- Password Hashing: Implemented using Django's built-in password hashing.
- Session Security: Implemented using Django's built-in session security.

Testing
- Registration: Test that a new user account can be created successfully.
- Login: Test that a user can log in successfully.
- Logout: Test that a user can log out successfully.
- Profile: Test that a user's profile information can be displayed and updated successfully.

