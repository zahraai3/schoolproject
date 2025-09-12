# School Management System

A simple Python application for managing school data including teachers, students, subjects, classes, and grades.

## What it does

This database system helps you manage:
- **Teachers** - Add, view, and update teacher information
- **Students** - Store student details and track their grades
- **Subjects** - Manage different school subjects
- **Classes** - Organize students into classes
- **Grades** - Track student performance and find top performers

## How to run

1. Make sure you have Python 3.12 installed
2. Install the required package:
   uv add sqlmodel
3. Run the application:
   uv run main.py

## What happens when you run it

The system will:
- Create a SQLite database file called `school.db`
- Set up all the necessary tables
- Currently shows students with high grades (80% and above)

## Main features

- **View all teachers** - See teacher names, subjects, and salaries
- **Add new teachers** - Register new teachers in the system
- **Update teacher info** - Change teacher names or salaries
- **View subjects and classes** - See which teachers teach what subjects
- **Find top students** - Celebrate students with excellent grades

## Database

The system uses SQLite database with these main tables:
- Students
- Teachers
- Subjects
- Classes
- Grades
- Class-Teacher relationships

## Files structure

- `main.py` - Main program file
- `database/` - Database related code
  - `models.py` - Database table definitions
  - `dbctrl.py` - Database connection
  - `crud.py` - Functions to add/view/update data
- `schoolinfo/info.py` - Sample data for testing

## Getting started

To add sample data to test the system, uncomment this line in `main.py`:
```python
# initialinformation()
```

Then run the program again to populate the database with example students, teachers, and grades.
## Worked on it :
- Zahraa Ibrahem
- Rafal Aesar
- Tabarak Ali