# we used a separated file for the connection with database and engine to get a cleaner code :) 
from sqlmodel import SQLModel,create_engine,Session


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args =  {"check_same_thread": False}

engine = create_engine(sqlite_url, connect_args= connect_args)
def creat_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session :
        yield session
