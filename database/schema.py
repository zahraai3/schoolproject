from typing import List
from sqlmodel import SQLModel, Field 


#---------------------------------TEACHER
#هذا كلاس سويته حتى اورث منه وحتى ما اضطر اكتب كلساع واعدل 
class Base(SQLModel):
    teacher_id: int | None = Field(default=None, foreign_key="teacher.id")
    class_id: int | None = Field(default=None, foreign_key="studentclass.id")

#هذا كلاس الانشاء الي يظهر بالفاست اي بي اي كريكوست المستخدم يدخل البيانات
class Creatc(Base):
    pass

#هذا كلاس عام سويته يظهر للمستخدم لان انا بالريكوست ما طلبت منه يدخل الايدي لكن هنا احتاج اطلع الايدي ف لازم نسوي كلاس ريسبونس
class Publicc(Base):
  id: int

#هذا كلاس للتحديثات المستخدم يعدل على المعلومات صحيح نفس المعلومات بكلاس الانشاء لكن :بكلاس الانشاء المستخدم مجبر يكتب البيانات المطلوبة لكن هنا : هو حيكون مخير شنو يريد يعدل احتاجيت اخلي هو بكيفه يعدل لولا مو الا كلهن
class Updatec(Base):
    teacher_id: int | None = None
    class_id: int | None = None

#نفس الملاحظات تم تطبيقهن على كلاس المعلم بالاسفل كما نلاحظ
class Teacherbase(SQLModel):
    name: str
    salary: int
    subject_id: int | None = Field(default=None, foreign_key="subject.id")
    
    
class Creatteacher(Teacherbase):
    pass

class Teacherpublic(Teacherbase):
    id: int
 

class Updateteacher(Teacherbase):
    name: str | None=None
    salary: int | None=None
    subject_id: int | None = None
    

#------------------------------------------STUDENT
# REQUEST BODY FOR CREATING A NEW STUDENT : 
class StudentCreate(SQLModel): 
    name : str
    age : int
    phone_num : str
    class_id: int | None = None

#RESPONSE MODEL TO READ STUDENT : 
class StudentRead(SQLModel):
    id :int
    name: str
    age: int
    phone_num : str
    class_id:int

#PUT/PATCH REQUEST BODY : 
class StudentUpdate(SQLModel):
    name: str | None = None
    age: int | None = None
    phone_num : str | None = None
    class_id : int | None = None


#STUDENT GRADE READ :
class StudentGradeRead(SQLModel) : 
    subject : "GradeSubjectread" 
    grade: int 

#GRADE CLASS READ RESPONSE MODEL : 
class GradeSubjectread(SQLModel) :
    name : str

#---------------------------FOR CLASS AND SUBJECT MATTERS
# موديل عرض للـ Subject فقط
class TeacherInSubjectRead(SQLModel):
    name: str
    salary: int

class SubjectRead(SQLModel):
    id: int
    name: str
    teachers: List[TeacherInSubjectRead] = []




