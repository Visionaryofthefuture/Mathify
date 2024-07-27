# Mathify

Mathify is an educational platform designed to help students learn mathematics through interactive courses and engaging content. The project is built using Django and provides a user-friendly interface for accessing various math courses.

## Features

- User registration and authentication
- Course management
- Interactive math courses with multimedia content
- Responsive design for mobile and desktop
- Secure email handling with environment variables
- A Chatbot Interface (work in progress) for students to ask and resolve their mathematics doubts with their critical thinking capabilities in mind.
  
## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Visionaryofthefuture/Mathify.git
   cd Mathify

2. **Create a virtual environment (not mandatory):**
  ```sh
     python -m venv venv
     source venv/bin/activate  # On Windows, use `venv\Scripts\activate

```
3. **Install Requirements**
   ```sh
   pip install -r requirements.txt

4. **Create a .env file in the mathify directory , you may move the empty .env from the root directory too**
  ```sh
  EMAIL_HOST=smtp.gmail.com
  EMAIL_PORT=587
  EMAIL_USE_TLS=True
  EMAIL_HOST_USER=your_email@gmail.com
  EMAIL_HOST_PASSWORD=your_email_password
  DEFAULT_FROM_EMAIL=your_email@gmail.com

```
5. **Apply migrations**
   ```sh
   python manage.py migrate

6. **Run the development server**
   ```sh
   python manage.py runserver

**Usage**

Access the application at http://localhost:8000.
Register as a new user and explore the available courses.
Admins can add and manage courses through the Django admin interface.
Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

**License**
This project is licensed under the MIT License.

**Contact**
For any inquiries, please contact me on linkedin  : https://www.linkedin.com/in/soumyajit-das-a46822251/

**Some Pictures of the simple interface**

![Screenshot from 2024-07-27 17-22-23](https://github.com/user-attachments/assets/8be82415-51f6-4c32-809c-59e2a00ed17b)

![Screenshot from 2024-07-27 17-22-50](https://github.com/user-attachments/assets/1e50ebe6-81a2-4009-8b4c-10b125e894fc)

![Screenshot from 2024-07-27 17-23-12](https://github.com/user-attachments/assets/f5681f05-da51-4ba0-b7c9-e0d4fa2de73d)

![Screenshot from 2024-07-27 17-23-44](https://github.com/user-attachments/assets/3c32ad5d-f56f-42e3-af99-e3faa6dfd5ae)

![Screenshot from 2024-07-27 17-23-55](https://github.com/user-attachments/assets/686924d4-f92e-4ff6-ba76-c906486c967e)

![Screenshot from 2024-07-27 17-25-40](https://github.com/user-attachments/assets/eac00dd3-ceeb-44d6-8996-297f3f19f3fa)
