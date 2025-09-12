from sqlmodel import Session, select
from database.models import Teacher,Student,Subject,studentClass
from database.dbctrl import engine


def select_teachers():
    with Session (engine) as session:
        statement = select(Teacher)
        result = session.exec(statement)
        print("")
        for teach in result:
            print(f"Teacher Name: {teach.name} , Subject: {teach.subject.name}, Salary: {teach.salary} ")
        print("")
      

def add_newteacher(teacher_name:str , teacher_salary:int):
    with Session (engine) as session:
        statement = select(Teacher). where (Teacher.name == teacher_name.strip())
        teachfound = session.exec(statement).first()
        print("")
        if teachfound:
            print(f"Teacher {teacher_name} is already in the system")
            
        else:
            newteacher =Teacher(name = teacher_name, salary = teacher_salary)
            session.add(newteacher)
            session.commit()
            session.refresh(newteacher)
            print(f"Teacher {newteacher.name} have been added to the system successfuly✅")
        print("")
            

     
def update_teacher(teacher_name: str, updated_salary: int | None = None, updated_name: str | None = None):
    print("")
    with Session(engine) as session:
        statement = select(Teacher).where(Teacher.name == teacher_name)
        teacher = session.exec(statement).first()

        if teacher:
            if updated_salary is not None:
                teacher.salary = updated_salary
            if updated_name is not None:
                teacher.name = updated_name

            session.commit()
            print(f"Teacher '{teacher.name}' has been updated ➡️  ",teacher)
        else:
            print(f"The teacher '{teacher_name}' does not exist ")
    print("")


def select_subjects():
    print("")
    with Session(engine) as session:
        statement= select(Subject)
        results= session.exec(statement)
        for sub in results:
            print(f" Subject: {sub.name}")
            if sub.teachers:
                for t in sub.teachers:
                    print(f" Teacher: {t.name}")
            else:
                print(" no teachers assigned yet")  
    print("")


def select_student_classes():
    print("")
    with Session(engine) as session:                              
        statement= select(studentClass) 
        results= session.exec(statement)
        for cls in results:
            print(f" Class: {cls.name}")
            if cls.students:
                for st in cls.students:
                    print(f" Student: {st.name}")
            else:
                print(" no students in this class yet")
    print("")


def high_grade():
    print("")
    print("🎉 Congratulations to our top students! 🎉\n")
    with Session(engine) as session:
        statement = select(Student)
        students = session.exec(statement).all()
        for student in students:
            if student.grades:
                avg = sum(g.grade for g in student.grades) / len(student.grades)
                if avg >= 80:
                    print(f"{student.name}: {avg:.2f} - Excellent performance! Keep up the great work🌟")
    print("")
    


def show_one_student(student_name):
    print("")
    with Session(engine) as session:
        # Find the student by his name
        student = session.exec(select(Student).where(Student.name == student_name)).first()
        if not student:
            print(f"Student '{student_name}' not found!")
        else:
        # Print info using relationships
        
            print(f"Student: {student.name}")
            print(f"Age: {student.age}")
            if student.student_class:
                print(f"Class: {student.student_class.name}")
            else:
                print("Class: None")

            print("Grades:")
            for grade in student.grades:
                print(f"  {grade.subject.name}: {grade.grade}")
                if student.grades:
                    avg = sum(g.grade for g in student.grades) / len(student.grades)
            print(f"➡️  Average :  {avg:.2f} ")
    print("")

