

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

     
def update_money(teacher_name: str, updated_salary: int | None = None, updated_name: str | None = None):
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

def select_subjects():
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

def select_student_classes():
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

def high_grade():
  print("🎉 Congratulations to our top students! 🎉\n")
  with Session(engine) as session:
      statement = select(Student)
      students = session.exec(statement).all()
      for student in students:
          if student.grades:
              avg = sum(g.grade for g in student.grades) / len(student.grades)
              if avg >= 80:
                print(f"{student.name}: {avg:.2f} - Excellent performance! Keep up the great work🌟")
    
              

    
    



def main ():

   # add_newteacher("MS rafal",3000)
#    update_money("Dr. Sarah Johnson",2000,None)
   # select_teachers()
   high_grade()
