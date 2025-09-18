from database.dbctrl import creat_db, engine, get_session
from sqlmodel import Session, select
from fastapi import  Depends, FastAPI, HTTPException
from database.models import * 
from schoolinfo.info import initialinformation

def main():
    creat_db()
    initialinformation()

if __name__ == "__main__":
    main()

app = FastAPI(
   title="School API",
    description="API for managing school data (students, teachers, classes).",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "Teacher",
            "description": "Operations related to teachers like creating, reading, updating.",
        },
        {
            "name": "Student",
            "description": "Endpoints for managing students data.",
        },
        {
            "name": "Class",
            "description": "Manage classes and their relationships with teachers/students ",
        },
    ]
) 


#//////////////////////////
#هذا البوست معناها المستخدم راح يكتب بيانات والبيانات هي نفسها الي ذكرتها بالكلاس الانشاء لازم يدخلهن وبعدها حفظتهن بالتيبل 
@app.post("/tacher/", response_model=Teacherpublic ,tags=["Teacher"])
def creat_teacher(teacher:Creatteacher):
    with Session (engine) as session:
        db_teacher = Teacher.model_validate(teacher)
        session.add(db_teacher)
        session.commit()
        session.refresh(db_teacher)
        return db_teacher

#هذا الكيت معناه  المستخدم  شنو يريد اطلعله ف هنا  اطلعله معلم واحد حسب الايدي الي يدخله
@app.get("/teacher/{teacher_id}", response_model=Teacherpublic ,tags=["Teacher"])
def read_teacher(teacher_id:int):
  with Session (engine) as session:
     teacher= session.get(Teacher, teacher_id)
     if not teacher:
       raise HTTPException(status_code=404, detail="teacher not found")#هذا ارفع خطا في حال المعلم ماكو 
     return teacher 

#هنا اطلع كل المعلمين للمستخدم واستخدمت لست لان الريسبونس مالتي راح يكون مجمومه ممكن
@app.get("/teacher/all_teachers", response_model=list[Teacherpublic] ,tags=["Teacher"])
def read_teachers():
    with Session (engine) as session:
     teacher= session.exec(select(Teacher)).all()
     return teacher
    
#هنا التعديل وراح يكون تعديل جزئي مو الا  المستخدم يعدل كل البيانات مالته هو مخير
@app.patch("/teacher/{teacher_id}", response_model=Teacherpublic ,tags=["Teacher"])
def update_teacher(teacher_id:int, teacher: Updateteacher):
    with Session (engine) as session:
      db_teacher= session.get(Teacher, teacher_id)
      if not db_teacher:
              raise HTTPException(status_code=404, detail="Teeacher not found")
      teacher_data = teacher.model_dump(exclude_unset=True)  #هذا ياخذ الاوبجكت ويشوف شنو عدلت وشنو ماعدلت ويروح يحدث التيبل القدديم يبقى نفسه والمتغير يتعدل
      db_teacher.sqlmodel_update(teacher_data) #احدث قاعدة البيانات
      session.add(db_teacher)
      session.commit()
      session.refresh(db_teacher)
      return db_teacher

#حذف معلم لما يتقاعد او ينفصل :)
@app.delete("/teacher/{teacher_id}", tags=["Teacher"])
def delete_teacher(teacher_id: int):
    with Session(engine) as session:
        db_teacher = session.get(Teacher, teacher_id)
        if not db_teacher:
            raise HTTPException(status_code=404, detail="Teacher not found")
        
        session.delete(db_teacher)
        session.commit()
        return {"message" : f"Teacher {db_teacher.name} deleted successfully "}
    
#//////////////////////////
#اضافه معلم للصف
@app.post("/class_teacher/", response_model=Publicc ,tags=["Class"])
def creat_classteach(classteach:Creatc):

  with Session (engine) as session:
    db_class = Classteacher.model_validate(classteach)
    session.add(db_class)
    session.commit()
    session.refresh(db_class)
    return db_class

#i used Depends here becasue there are some issues with session and relation had happened so yeah 
#show the subjects and their teachers :
@app.get('/subjects/{id}', response_model=SubjectRead , tags=["Class"])
def select_subject(*, id: int, session: Session = Depends(get_session)):
    db_subject = session.get(Subject, id)
    if not db_subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return db_subject

#read a single student :
@app.get("/students/{student_id}",tags=["Student"],response_model=StudentRead)
def get_student(student_id: int):
    with Session(engine) as session :
      student = session.get(Student, student_id)
      if not student:
          raise HTTPException(status_code=404, detail="Student not found")
      return student

#read a student grades 
@app.get("/students/{student_id}/grades", response_model=list[StudentGradeRead],tags=["Student"])
def get_student_grades(student_id: int, session: Session = Depends(get_session)):
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    # حته نرجع الدرجات 
    result = []
    for grade in student.grades:
        item = StudentGradeRead(
            subject=GradeSubjectread(name=grade.subject.name),
            grade=grade.grade
        )
        result.append(item)
    return result

#adding a new student :
@app.post("/student/new_student", response_model=StudentCreate ,tags=["Student"])
def creat_student(new_student:StudentCreate):
    with Session (engine) as session:
        db_student = Student.model_validate(new_student)
        session.add(db_student)
        session.commit()
        session.refresh(db_student)
        return db_student

#deleting a student :
@app.delete("/student/{student_id}", tags=["Student"])
def delete_student(student_id: int):
    with Session(engine) as session:
        db_student = session.get(Student, student_id)
        if not db_student:
            raise HTTPException(status_code=404, detail="Student not found")
        
        session.delete(db_student)
        session.commit()
        return {"message" : f"Student {db_student.name} deleted successfully "}

#edditing a student info :
@app.patch("/student/{student_id}", response_model=StudentUpdate ,tags=["Student"])
def update_student(student_id:int, updated_student: StudentUpdate):
    with Session (engine) as session:
      db_student= session.get(Student, student_id)
      if not db_student:
              raise HTTPException(status_code=404, detail="Student not found")
      student_data = updated_student.model_dump(exclude_unset=True)  
      db_student.sqlmodel_update(student_data) 
      session.add(db_student)
      session.commit()
      session.refresh(db_student)
      return db_student


