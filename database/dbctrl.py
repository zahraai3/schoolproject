# we used a separated file for the connection with database and engine to get a cleaner code :) 
from sqlmodel import SQLModel,create_engine,Session
from fastapi import FastAPI,HTTPException 


sqlite_file_name = "school.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url) 

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session :
        yield session


