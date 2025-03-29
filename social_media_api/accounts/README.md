# Social Media API

This is a social media API built with Django and Django REST Framework.

## Setup
1. Clone the repository: `git clone https://github.com/your-username/social-media-api.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Run the migrations: `python manage.py migrate`
4. Start the development server: `python manage.py runserver`

## API Endpoints
### Registration
* `POST /register/`: Register a new user.
	+ Request Body: `username`, `email`, `password`, `bio`, `profile_picture`
	+ Response: `token`

### Login
* `POST /login/`: Login an existing user.
	+ Request Body: `username`, `password`
	+ Response: `token`

### Profile
* `GET /profile/`: Get the current user's profile.
	+ Response: `username`, `email`, `bio`, `profile_picture`, `followers`

