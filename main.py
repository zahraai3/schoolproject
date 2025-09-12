from database.dbctrl import create_db_and_tables
from schoolinfo.info import initialinformation
from database.crud import main
from database.crud import update_money,select_teachers,add_newteacher,select_subjects,select_student_classes

def main():
    create_db_and_tables()
    initialinformation()
    #update_money()
    #select_teachers()
    #add_newteacher()
    select_subjects()
    select_student_classes()

if __name__ == "__main__":
    main()