from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .. import config

SQLALCHEMY_DATABASE_URL = config.setting.SQLALCHEMY_DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)

base = declarative_base()

#depend
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
