# we used a separated file for the connection with database and engine rule to get a cleaner code :) 
from sqlmodel import SQLModel,Session,create_engine

sqlite_file_name = "school.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True) # echo - so all sql commands be shown in the console 

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

