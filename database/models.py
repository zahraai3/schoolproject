from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from database.schema import*


#for students
class Student(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int
    phone_num: str
    class_id: int | None = Field(default=None, foreign_key="studentclass.id")

    grades: Optional[List["Grade"]] = Relationship(back_populates="student")
    student_class: Optional["studentClass"] = Relationship(back_populates="students")

# for the students grades
class Grade(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    grade: int
    student_id: int | None = Field(default=None, foreign_key="student.id")
    subject_id: int | None = Field(default=None, foreign_key="subject.id")

    student: Optional["Student"] = Relationship(back_populates="grades")
    subject: Optional["Subject"] = Relationship(back_populates="grades")

#the subject 
class Subject(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)

    grades: Optional[List["Grade"]] = Relationship(back_populates="subject")
    teachers: Optional[List["Teacher"]] = Relationship(back_populates="subject")

# class
class studentClass(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str

    students: Optional[List["Student"]] = Relationship(back_populates="student_class")
    teacherclass: Optional[List["Classteacher"]] = Relationship(back_populates="classes")

# to know what class take each teacher
#هذا كلاس مودل تيبل الاساسي الي حيكون بي اعمده يربط بي المعلم والصف
class Classteacher(Base, table = True):
    id: int | None = Field(default=None, primary_key=True)
    teacher: Optional["Teacher"] = Relationship(back_populates="teacher_class")
    classes: Optional["studentClass"] = Relationship(back_populates="teacherclass")


    


#هذا هم اساسي يحتوي على معلم ويحتاج الى مادة
class Teacher(Teacherbase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    teacher_class: list["Classteacher"]= Relationship(back_populates="teacher")
    subject: Optional["Subject"] = Relationship(back_populates="teachers")

    
