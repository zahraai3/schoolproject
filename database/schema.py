from sqlmodel import SQLModel, Field

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
    
