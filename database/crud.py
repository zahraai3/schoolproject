

from sqlmodel import Session, select
from database.models import Teacher
from database.dbctrl import engine


def select_teacher():
  with Session (engine) as session:
     statement = select(Teacher)
     result = session.exec(statement)
     for teach_all in result:
        print (teach_all)



def add_newteacher():
  teacher5 =Teacher(name = " Dr. Aseel Aesar", salary = 40000)
  with Session (engine) as session:
     session.add(teacher5)
     session.commit()
     session.refresh(teacher5)

     
def update_money():
  with Session (engine) as session:
   statement = select( Teacher ).where (Teacher.name == "Dr. Sarah Johnson")
   result = session.exec(statement)
  #  teacher = result.one() 

  # او استخرم firstفي حال الاسم مايكون موجود او موجود اكثر من مرة
   teacher = result.first()
   if teacher:  #يتحقق لذا المعلم موجود او موجود اكثر من مرة واذا ماكو راح يرجع none
    
    teacher.salary = 60000
    session.commit()



def main ():
   add_newteacher()
   update_money()
   select_teacher()

if __name__ == "__main__":
     main()