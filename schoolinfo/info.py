from sqlmodel import Session
from database.models import Student,Grade,studentClass,Teacher,Subject,classTeacher
from database.dbctrl import engine

sqlite_file_name = "school.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"


def initialinformation() :
    with Session(engine) as session :
        subjects_data = [
            Subject(name="Mathematics"),
            Subject(name="English Literature"),
            Subject(name="Physics"),
            Subject(name="Chemistry"),
            Subject(name="History"),
            Subject(name="Biology")
        ]

        session.add_all(subjects_data)
        session.commit()
        print("|||||||| : added subject data")


        classes_data = [
            studentClass(name="Class A"),
            studentClass(name="Class B")
        ]

        session.add_all(classes_data)
        session.commit()
        print("|||||||| : added classes data")

 
        teachers_data = [
            Teacher(name="Dr. Sarah Johnson", salary=55000, subject_id=subjects_data[0].id),  # Math
            Teacher(name="Prof. Michael Brown", salary=52000, subject_id=subjects_data[1].id),  # English
            Teacher(name="Dr. Emily Davis", salary=58000, subject_id=subjects_data[2].id),  # Physics
            Teacher(name="Mr. David Wilson", salary=50000, subject_id=subjects_data[3].id)   # Chemistry
        ]

        session.add_all(teachers_data)
        session.commit()
        print("|||||||| : added teachera data")

        
        class_teacher_data = [
            classTeacher(teacher_id=teachers_data[0].id, class_id=classes_data[0].id), 
            classTeacher(teacher_id=teachers_data[1].id, class_id=classes_data[0].id),  
            classTeacher(teacher_id=teachers_data[2].id, class_id=classes_data[1].id),  
            classTeacher(teacher_id=teachers_data[3].id, class_id=classes_data[1].id)   
        ]

        session.add_all(class_teacher_data)
        session.commit()
        print("|||||||| : added CLASSTEACHER data")


        students_data = [
            # Class A 
            Student(name="Alice Smith", age=16, phone_num="123-456-7890", class_id=classes_data[0].id),
            Student(name="Bob Johnson", age=17, phone_num="123-456-7891", class_id=classes_data[0].id),
            Student(name="Charlie Brown", age=16, phone_num="123-456-7892", class_id=classes_data[0].id),
            Student(name="Diana Prince", age=17, phone_num="123-456-7893", class_id=classes_data[0].id),
            Student(name="Edward Norton", age=16, phone_num="123-456-7894", class_id=classes_data[0].id),
            Student(name="Fiona Green", age=17, phone_num="123-456-7895", class_id=classes_data[0].id),
            Student(name="George Miller", age=16, phone_num="123-456-7896", class_id=classes_data[0].id),
            Student(name="Hannah Davis", age=17, phone_num="123-456-7897", class_id=classes_data[0].id),
            
            # Class B 
            Student(name="Ian Wilson", age=16, phone_num="123-456-7898", class_id=classes_data[1].id),
            Student(name="Julia Roberts", age=17, phone_num="123-456-7899", class_id=classes_data[1].id),
            Student(name="Kevin Hart", age=16, phone_num="123-456-7900", class_id=classes_data[1].id),
            Student(name="Laura Thompson", age=17, phone_num="123-456-7901", class_id=classes_data[1].id),
            Student(name="Mark Anderson", age=16, phone_num="123-456-7902", class_id=classes_data[1].id),
            Student(name="Nina Garcia", age=17, phone_num="123-456-7903", class_id=classes_data[1].id),
            Student(name="Oliver Stone", age=16, phone_num="123-456-7904", class_id=classes_data[1].id)
        ]

        session.add_all(students_data)
        session.commit()
        print("|||||||| : added students data")


        grades_data = []
        
        # Give each student grades in multiple subjects
        for i, student in enumerate(students_data):
            # Each student gets grades in 3-4 subjects
            if i < 8:  # Class A students - Math, English, Physics
                grades_data.extend([
                    Grade(grade=90  + i, student_id=student.id, subject_id=subjects_data[0].id),  # Math
                    Grade(grade=60 + i , student_id=student.id, subject_id=subjects_data[1].id),  # English
                    Grade(grade=88 + i , student_id=student.id, subject_id=subjects_data[2].id)   # Physics
                ])
            else:  # Class B students - Chemistry, History, Biology
                grades_data.extend([
                    Grade(grade=80 - i , student_id=student.id, subject_id=subjects_data[3].id),  # Chemistry
                    Grade(grade=75 - i , student_id=student.id, subject_id=subjects_data[4].id),  # History
                    Grade(grade=99 - i, student_id=student.id, subject_id=subjects_data[5].id)   # Biology
                ])

        session.add_all(grades_data)
        session.commit()
        print("|||||||| : added grades data")




