

from sqlmodel import Session, select
from database.models import Teacher
from database.dbctrl import engine


def select_teacher():
  with Session (engine) as session:
     statement = select(Teacher)
     result = session.exec(statement)
     for teach in result:
        print(f"ID: {teach.id}, Name teacher : {teach.name}, Salary = {teach.salary}")


def add_newteacher():
    with Session (engine) as session:
       statement = select(Teacher). where (Teacher.name == "Dr. Aseel Aesar")
       teachfound = session.exec(statement).first()
       if teachfound:
          print("the teacher 'Dr. Aseel Aesar' already exists")
       else:
          
          teacher5 =Teacher(name = " Dr. Aseel Aesar", salary = 40000)
          session.add(teacher5)
          session.commit()
          session.refresh(teacher5)

     
def update_money():
  with Session (engine) as session:
   statement = select( Teacher ).where (Teacher.name == "Dr. Sarah Johnson")
   teacher = session.exec(statement).first()


   if teacher :
      print("the teacher 'Dr. Sarah Johnson' exists")
  # او استخرم firstفي حال الاسم مايكون موجود او موجود اكثر من مرة
      # if teacher:  #يتحقق لذا المعلم موجود او موجود اكثر من مرة واذا ماكو راح يرجع none
    
      teacher.salary = 60000
      session.commit()
   else:
      print("the teacher not exist")



def main ():

   # add_newteacher()
   # update_money()
   select_teacher()

if __name__ == "__main__":
     main()