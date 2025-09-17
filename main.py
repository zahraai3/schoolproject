# from database.dbctrl import create_db_and_tables
# from schoolinfo.info import initialinformation
# from database.crud import  select_teachers,add_newteacher,update_teacher,select_subjects,select_student_classes,high_grade,show_one_student


# def main():
#     create_db_and_tables()
#     # initialinformation()
#     # select_teachers()
#     # add_newteacher("Dr.atheer",300)
#     # update_teacher("Dr.atheer",440,None)
#     # select_subjects()
#     # select_student_classes()
#     # high_grade()
#     show_one_student("Nina Garcia")

# if __name__ == "__main__":
#     main()





from database.models import * 


from sqlmodel import SQLModel, create_engine, Session, select
from fastapi import FastAPI, HTTPException, Query

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args =  {"check_same_thread": False}

engine = create_engine(sqlite_url, echo=True, connect_args= connect_args)
def creat_db():
 SQLModel.metadata.create_all(engine)

  
#هاي دالة سويتها حتى تفعل الداتا بس مالتي مرة وحدة
app = FastAPI() 
@app.on_event("startup")

#هاي دالة سويتها حتى تفعل الداتا بس مالتي مرة وحدة

def on_startup():
  creat_db()


  #هذا البوست معناها المستخدم راح يكتب بيانات والبيانات هي نفسها الي ذكرتها بالكلاس الانشاء لازم يدخلهن وبعدها حفظتهن بالتيبل 
@app.post("/tacher/", response_model=Teacherpublic)
def creat_teacher(teacher:Creatteacher):

  with Session (engine) as session:
    db_teacher = Teacher.model_validate(teacher)
    session.add(db_teacher)
    session.commit()
    session.refresh(db_teacher)
    return db_teacher

#هذا الكيت معناه  المستخدم  شنو يريد اطلعله ف هنا  اطلعله معلم واحد حسب الايدي الي يدخله
@app.get("/teacher/{teacher_id}", response_model=Teacherpublic)
def read_teacher(teacher_id:int):
  with Session (engine) as session:
     teacher= session.get(Teacher, teacher_id)
     if not teacher:
       raise HTTPException(status_code=404, detail="teacher not found")#هذا ارفع خطا في حال المعلم ماكو 
     return teacher 


#هنا اطلع كل المعلمين للمستخدم واستخدمت لست لان الريسبونس مالتي راح يكون مجمومه ممكن
@app.get("/teacher/", response_model=list[Teacherpublic])
def read_teacher():
    with Session (engine) as session:
     teacher= session.exec(select(Teacher)).all()
     return teacher
    
#هنا التعديل وراح يكون تعديل جزئي مو الا  المستخدم يعدل كل البيانات مالته هو مخير
@app.patch("/teacher/{teacher_id}", response_model=Teacherpublic)
def update_teacher(teacher_id:int, teacher: Updateteacher):
    with Session (engine) as session:
      db_teacher= session.get(Teacher, teacher_id)
      if not db_teacher:
              raise HTTPException(status_code=404, detail="Hero not found")
      teacher_data = teacher.model_dump(exclude_unset=True)  #هذا ياخذ الاوبجكت ويشوف شنو عدلت وشنو ماعدلت ويروح يحدث التيبل القدديم يبقى نفسه والمتغير يتعدل
      db_teacher.sqlmodel_update(teacher_data) #احدث قاعدة البيانات
      session.add(db_teacher)
      session.commit()
      session.refresh(db_teacher)
      return db_teacher





@app.post("/class_teacher/", response_model=Publicc)
def creat_classteach(classteach:Creatc):

  with Session (engine) as session:
    db_class = Classteacher.model_validate(classteach)
    session.add(db_class)
    session.commit()
    session.refresh(db_class)
    return db_class
