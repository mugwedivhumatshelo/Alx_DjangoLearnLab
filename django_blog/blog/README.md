Authentication System Documentation
Overview
The authentication system is a critical component of the Django blog project, enabling users to register, login, and manage their profiles. This documentation provides a detailed overview of the authentication system, including its components, functionality, and testing instructions.

Components
The authentication system consists of the following components:

1. Registration: Allows users to create a new account by providing a username, email, and password.
2. Login: Enables users to access their account by entering their username and password.
3. Profile Management: Allows users to update their profile information, including their email address.
4. Logout: Enables users to log out of their account.

Authentication Process
The authentication process involves the following steps:

1. Registration:
    - User submits a registration form with their username, email, and password.
    - The system checks for duplicate usernames and emails.
    - If the registration is successful, the user is redirected to the login page.
2. Login:
    - User submits a login form with their username and password.
    - The system checks the username and password against the stored credentials.
    - If the login is successful, the user is redirected to the dashboard.
3. Profile Management:
    - User accesses their profile page.
    - User updates their profile information, including their email address.
    - The system saves the updated profile information.
4. Logout:
    - User clicks the logout button.
    - The system logs the user out and redirects them to the login page.

Testing Instructions
To test each authentication feature, follow these instructions:

1. Registration:
    - Go to the registration page (http://localhost:8000/register/).
    - Fill out the registration form with valid data.
    - Submit the form and verify that the user is created successfully.
2. Login:
    - Go to the login page (http://localhost:8000/login/).
    - Fill out the login form with valid data.
    - Submit the form and verify that the user is logged in successfully.
3. Profile Management:
    - Go to the profile page (http://localhost:8000/profile/).
    - Update the profile information, including the email address.
    - Submit the form and verify that the profile information is updated successfully.
4. Logout:
    - Go to the dashboard page (http://localhost:8000/).
    - Click the logout button.
    - Verify that the user is logged out and redirected to the login page.

