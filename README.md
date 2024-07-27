# Mathify

Mathify is an educational platform designed to help students learn mathematics through interactive courses and engaging content. The project is built using Django and provides a user-friendly interface for accessing various math courses.

## Features

- User registration and authentication
- Course management
- Interactive math courses with multimedia content
- Responsive design for mobile and desktop
- Secure email handling with environment variables

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Visionaryofthefuture/Mathify.git
   cd Mathify

2. **Create a venv (optional) **

  python -m venv venv
  source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. pip install -r requirements.txt

4. Create a .env file in the mathify directory , you may move the empty .env from the root directory too
  EMAIL_HOST=smtp.gmail.com
  EMAIL_PORT=587
  EMAIL_USE_TLS=True
  EMAIL_HOST_USER=your_email@gmail.com
  EMAIL_HOST_PASSWORD=your_email_password
  DEFAULT_FROM_EMAIL=your_email@gmail.com

5. Apply migrations

   python manage.py migrate

6. Run the development server

   python manage.py runserver


    
