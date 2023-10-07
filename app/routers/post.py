from typing import Optional
from fastapi import APIRouter, Depends,status
from ..orm_db.database import get_db
from ..orm_db.schemas import postId, userCreate, createUserRespones,postCreate
from sqlalchemy.orm import Session
from ..import oauth2
from ..orm_db import models_orm
from ..orm_db import crud


router =APIRouter(prefix="/posts" ,tags=["posts"])


@router.get("/")
#/?limit=20  می شود لیمت را از طریق یو ار ال تغییر داد
def get_all_posts(limit:int =10, skip:int =0,keyword:Optional[str]="" ,  db:Session=Depends(get_db)):
      return crud.get_all_posts(db ,limit,skip,keyword)
      
      
@router.post("/")
def create_post(post:postCreate, db:Session=Depends(get_db) ,current_user:models_orm.user_db=Depends(oauth2.get_currnt_user)):
      a =crud.create_post(db,post,current_user.id)
      return {"message":"Post Successfully created",
              "post_id": a.id,
              "title": a.title,
              "content": a.content,
              "time_Created": a.time_Created,
              "author_username" : current_user.username,
              "owner_id": a.owner_id,
            "owner ":a.owner
              }
      
@router.delete("/")
def delete_post(postid:postId,db:Session=Depends(get_db),current_user:models_orm.user_db=Depends(oauth2.get_currnt_user)):
      crud.delete_post(postid.post_id,db,current_user)
      return{"massege":f"post({postid.post_id}) deleted."}
      
      
      