from sqlalchemy.orm import Session
from .schemas import postId, user,userCreate,postCreate
from .models_orm import user_db,post_db
from fastapi import HTTPException,status
from passlib.context import CryptContext
pw_content= CryptContext(schemes="bcrypt",deprecated="auto")

def createuser(db:Session,user_info:userCreate):
      user_from_db=db.query(user_db).filter(user_db.username==user_info.username).first()
      
      if not user_from_db:
            #if user name alrady exist get_user function rasie 404 error
            hash_password=pw_content.hash(user_info.password)
            user_info.password=hash_password
            new_user=user_db(**user_info.model_dump())
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return new_user
      else:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,detail=f"username({user_info.username}) already exist ")

def get_users(db:Session):
      data_base_tuple_result=db.query(user_db.username ,user_db.id,user_db.sinup_data).all()
      
      dict_result=[{"username":username,"id":id,"sinupDate":sinupDate} 
       for username ,id, sinupDate in data_base_tuple_result
      ]
      return dict_result
     
      
def get_user(db: Session, username: str):
      target_user_tuple= db.query(user_db.username ,user_db.id,user_db.email).filter(user_db.username == username).first()
      print(target_user_tuple)
      if target_user_tuple:
            dict_result= {"username":target_user_tuple[0],"id":target_user_tuple[1],"email":target_user_tuple[2]}
            return dict_result
      else:
            raise HTTPException(status_code=404,detail="User name not found")
    
def delete_all_users(db:Session):
      db.query(user_db).delete()
      db.commit()
      raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)

#___________________posts ______________________________

def create_post(db:Session,post:postCreate,owner_id):
      
      new_post= post_db(title=post.title,content=post.content,owner_id=owner_id)
      db.add(new_post)
      db.commit()
      db.refresh(new_post)
      return new_post
      
def get_all_posts(db:Session , limit:int , skip:int,keyword:str):
      
      return db.query(post_db).filter(post_db.title.contains(keyword)).limit(limit).offset(skip).all()

def delete_post(post_id,db:Session,current_user:user_db):
      #get post from db 
      
      post_query= db.query(post_db).filter(post_db.id==post_id)
      if post_query.first() == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail= f"There is no post with the given id({post_id})")
      elif post_query.first().owner_id != current_user.id :
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"you can not delete this post({post_id}) because your not author.")
      post_query.delete()
      db.commit()
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      