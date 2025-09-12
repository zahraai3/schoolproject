from database.dbctrl import create_db_and_tables
from schoolinfo.info import initialinformation
from database.crud import  select_teachers,add_newteacher,update_teacher,select_subjects,select_student_classes,high_grade


def main():
    create_db_and_tables()
    # initialinformation()
    # select_teachers()
    # add_newteacher("Dr.atheer",300)
    # update_teacher("Dr.atheer",440,None)
    # select_subjects()
    # select_student_classes()
    high_grade()

if __name__ == "__main__":
    main()