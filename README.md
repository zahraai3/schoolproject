# School Management FastAPI with SQLModel

A RESTful API built with FastAPI and SQLModel for managing school data including students, teachers, classes, subjects, and grades.

## ✨ Features

- **Student Management**: Create, read, update, and delete student records
- **Teacher Management**: Manage teacher information and subject assignments
- **Class Organization**: Organize students into classes and assign teachers
- **Grade Tracking**: Track student grades across different subjects
- **Subject Management**: Manage academic subjects and their assigned teachers
- **Automatic Database Setup**: Pre-populated with sample data for testing


## 📁 Project Structure

```
schoolproject/
├── database/
│   ├── dbctrl.py          # Database connection and session management
│   ├── models.py          # SQLModel database models
│   └── schema.py          # Pydantic schemas for API requests/responses
├── schoolinfo/
│   └── info.py            # Initial data population
├── main.py                # FastAPI application and endpoints
├── pyproject.toml         # Project dependencies
├── .python-version        # Python version specification
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

## 🚀 To See the project code :

 **Clone the repository**
   git clone <https://github.com/zahraai3/schoolproject.git>
   cd schoolproject
   
 **Initialize the database**
   uv run main.py

 **Run the application**
   uv run fastapi run

The API will be available at `http://localhost:8000`

## 📖 Usage

### Interactive API Documentation

Once the server is running, you can access:

- **Swagger UI**: `http://localhost:8000/docs`

### Sample Data

The application automatically creates sample data including:
- 6 subjects (Mathematics, English Literature, Physics, Chemistry, History, Biology)
- 2 classes (Class A, Class B)
- 4 teachers assigned to different subjects
- 15 students distributed across classes
- Grade records for all students

## 🔌 API Endpoints

### Teachers

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/teacher/` | Create a new teacher |
| `GET` | `/teacher/{teacher_id}` | Get teacher by ID |
| `GET` | `/teacher/all_teachers` | Get all teachers |
| `PATCH` | `/teacher/{teacher_id}` | Update teacher information |
| `DELETE` | `/teacher/{teacher_id}` | Delete a teacher |

### Students

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/students/{student_id}` | Get student by ID |
| `GET` | `/students/{student_id}/grades` | Get student's grades |
| `POST` | `/student/new_student` | Create a new student |
| `PATCH` | `/student/{student_id}` | Update student information |
| `DELETE` | `/student/{student_id}` | Delete a student |

### Classes & Subjects

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/class_teacher/` | Assign teacher to class |
| `GET` | `/subjects/` | Get all subjects with teachers |
| `GET` | `/subjects/{subject_id}` | Get subject by ID |
| `GET` | `/classes/` | Get all classes with students |
| `GET` | `/classes/{class_id}` | Get class by ID |

## 🗃️ Database Schema

The database consists of the following main entities:

- **Student**: Student information and class assignment
- **Teacher**: Teacher details and subject specialization
- **Subject**: Academic subjects
- **studentClass**: Class information
- **Grade**: Student grades in specific subjects
- **Classteacher**: Many-to-many relationship between teachers and classes

## 👩🏻‍💻Worked on this project :
- Tabarak Ali
- Rafal Aesar
- Zahraa Ibrahem