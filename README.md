## First OAuth (Github)

Authentication using OAuth 2.0 (GitHub)

## Technologies 

- Python 3.12
- Django 
- django-allauth
- OAuth 2.0 (GitHub)

## Functions

- GitHub social login
- OAuth 2.0 authentication flow
- Protected member-only page (login_required)
- Login and Logout functionality

## Setup

### Clone the repository

```bash
git clone https://github.com/nickezinho/first_oauth.git
cd first_oauth
```
### Activate a virtual enviroment and install de requirements
```bash
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
```

### Create a .env file
```env
CLIENT_ID_GITHUB=your_client_id
SECRET_GITHUB=your_secret_id
```
### Run migrations and server

```bash
python manage.py migrate
python manage.py runserver
```

### (🚨) Access the running application at:

```md
Open in your browser:

[http://localhost:8000](http://localhost:8000)
```
# Authentication Flow

- Click on the GitHub logo
- Authorize the application
- You will be redirected to the members-only page

# Notes

- This project was intended for learning and demo only!
- OAuth secrets are stored securely using env variables
