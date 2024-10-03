# Django ToDo List App

## Overview

This is a simple ToDo List application built with Django, marking my first experience with the framework. The app provides functionalities for user registration, login, creating to-do lists, and viewing them. My goal is to enhance my skills in Django and continue improving in the future.

## Features

- User registration
- User login
- Create new to-do lists
- View existing to-do lists
- Mark items as complete

## URL Paths

- `/`: Home page
- `/register/`: Registration page for new users
- `/login/`: Login page for existing users
- `/create/`: Page to create a new to-do list
- `/<int:id>`: View a specific to-do list by ID

## Getting Started

To run the app locally, clone the repository and follow the instructions below:

1. **Install Dependencies**: Ensure you have Django installed. You can install it via pip:
   ```bash
   pip install django
   ```

2. **Run Migrations**: Apply the migrations to set up your database.
   ```bash
   python manage.py migrate
   ```

3. **Run the Development Server**: Start the server with:
   ```bash
   python manage.py runserver
   ```

4. **Access the App**: Open your web browser and go to `http://127.0.0.1:8000/` to access the application.

## Acknowledgments

I would like to express my gratitude for the resources and community support that helped me during the development of this application. I'm excited to continue learning and improving my skills in Django.
