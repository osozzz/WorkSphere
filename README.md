# WorkSphere

WorkSphere is a web application that centralizes and personalizes information about upcoming events based on users' interests. It allows users to perform personalized searches, receive notifications with updated information, and facilitates both event registration and ticket purchases. The application also integrates social interaction features and generates a QR code for event check-ins.

## Requirements

To run this project, you will need:

- Python 3.12.7
- Django 5.1.1
- SQLite3 (or your preferred database)
- pip (Python package manager)
- Git (version control)

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/osozzz/WorkSphere.git
   cd WorkSphere
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**

   Apply the migrations to set up your database schema.

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**

   This will allow you to access the Django admin panel.

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   Start the local development server and access the application in your browser.

   ```bash
   python manage.py runserver
   ```

   The application should now be available at `http://127.0.0.1:8000/`.

