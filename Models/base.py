from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DBA_NAME = os.getenv('DBA_NAME')
DBA_USER = os.getenv('DBA_USER')
DBA_PASS = os.getenv('DBA_PASS')
DBA_HOST = os.getenv('DBA_HOST')
DBA_PORT = os.getenv('DBA_PORT')
DATABASE_URI = f'mysql+pymysql://{DBA_USER}:{DBA_PASS}@{DBA_HOST}:{DBA_PORT}/{DBA_NAME}'

engine = create_engine(DATABASE_URI, echo=True)

Session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)

def shutdown_session(exception=None):
    Session.remove()