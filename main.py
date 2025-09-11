from database.dbctrl import create_db_and_tables,engine
from database.models import Student,Grade,studentClass,Teacher,Subject,classTeacher

from sqlmodel import Session
from schoolinfo.info import initialinformation

# def main():
#     create_db_and_tables()
#     initialinformation()

# if __name__ == "__main__":
#     main()