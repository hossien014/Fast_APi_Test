'''این مدل ها مربوط به پایدنتیک هستند  و برای اینکه 
      با مدل های اس کیو ال اشتباه گرفته نشوند اسم این فایل اسکیما است
'''
from pydantic import BaseModel,EmailStr, conint
from datetime import datetime


from typing import List,Dict, Optional


class simpleRespones(BaseModel):
      #جواب یک دیکشنری است به اسم رسیپاند 
      # که حاوی یک لیست از دیکشنری هایی است که کی انها استرینکو ولیو انها اینت است
      respones:list[dict[str,int]]
#_____________________ USERS_________________________________
class createUserRespones(BaseModel):
      msg:str
      info:dict
      

class userBase(BaseModel):
      username:str
      email:EmailStr |None
      
      class Config:
                  orm_mode = True

class userCreate(userBase):
      password:str

class user(userBase):
      id:int
      # sinup_data:date
      
class userCredentials(BaseModel):
      username:str
      password:str

      
class TokenData(BaseModel):
    id: int = None
    
#_________________POSTS__________________________

class postBase(BaseModel):
      title:str
      content:str

class postCreate(postBase):
      pass

class post(postBase):
      id:int
      time_created:datetime
      owner_id:int
      owner:user
      class conficg():
            orm_mode=True
      
class postId(BaseModel):
      post_id:int
      
class post_out:
      post: post
      
class vote_input(BaseModel):
      post_id :int
      # یعنی عدد ورودی باید یک یا کمتر از یک باشد
      dir :conint(le=1)
      