from fastapi import APIRouter, Depends,status
from ..orm_db.database import get_db
from ..orm_db.schemas import userCreate, createUserRespones
from sqlalchemy.orm import Session
from ..import oauth2
from ..orm_db import models_orm
from ..orm_db import crud



router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def get_all_users(db: Session = Depends(get_db) ,current_user=Depends(oauth2.get_currnt_user)):
    return crud.get_users(db)


@router.post("/", response_model=createUserRespones,status_code=status.HTTP_201_CREATED)
def create_user(user_info: userCreate, db: Session = Depends(get_db)):
      new_user = crud.createuser(db, user_info)
      return {"msg": f"user created successfully", "info": {"username ": new_user.username, "sinup_date": new_user.sinup_data, "email": new_user.email}}

@router.delete("/")
def Delete_all_users( db: Session = Depends(get_db)):
    crud.delete_all_users(db)


@router.get('/{username}')
def get_user(username: str, db: Session = Depends(get_db)):
    return crud.get_user(db, username)
