from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:20102009@localhost/alchemy"

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
