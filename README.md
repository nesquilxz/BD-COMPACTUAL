# Flask User Registration System

This project is a simple web application built with **Flask** and **SQLite** that allows users to register, store, and search personal data through a web interface. It simulates a basic CRUD-style system commonly used in internal tools, administrative panels, and small web applications.

The main goal of this project is to demonstrate fundamental concepts of backend development, database integration, and request handling using Python.

## Technologies Used
- Python
- Flask
- SQLite
- HTML 

## Features
- User registration via web form
- Persistent data storage using SQLite
- Listing all registered users
- Search users by name
- Automatic database and table creation
- Simple routing and request handling

## Project Structure
- `app.py`: Main application file containing routes, database logic, and Flask configuration
- `templates/`
  - `form.html`: User registration form
  - `lista.html`: Page to list and search registered users
- `cadastro.db`: SQLite database (created automatically)

## How It Works
- When the application starts, it automatically creates a database and table if they do not exist
- Users can register by submitting a form with name, email, and age
- The data is stored in a SQLite database
- A listing page displays all users and allows filtering by name using a search field

## How to Run
1. Install the dependencies:
   ```bash
   pip install flask
