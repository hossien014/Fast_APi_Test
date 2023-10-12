'''
اینجا جایی که که ما شروع میکنیم به ساخت جدول های مختلف دیتا بیس .
هر کلاس در اینجا نماینده یک جدول در دیتا بیس است 
اگر جدول وجود داشته باشد ان را نمی ساز وگرنه ان را میسازد
'''
#  مدل های این فایل مربوط به دیتا بیس است نه پایدنتیک
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.orm import relationship
from .database import base
# تمام کلاس های که میسازیم باید از بیس که در فایل دیتا بیس وجود دارد ارث بری کنند

class user_db(base):
      
      __tablename__="users"
      
      id=Column(Integer,nullable=False,index=True ,primary_key=True)
      username=Column(String,nullable=False,unique=True)
      password=Column(String,nullable=False)
      email=Column(String,nullable=True)
      sinup_data=Column(DateTime ,server_default="now()" )
      
class post_db(base):
      __tablename__="posts"
      id= Column(Integer,nullable=False,index=True,primary_key=True)
      title=Column(String,nullable=False)
      content=Column(String)
      time_Created =Column(DateTime ,server_default="now()")
      owner_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE") ,nullable=False)
      
      owner=relationship("user_db")
      
class vote_db(base):
      __tablename__="votes"
      user_id=Column(Integer,
                     ForeignKey("users.id",ondelete="CASCADE")
                     ,nullable=False
                     ,primary_key=True, )
      
      post_id=Column(Integer,
                     ForeignKey("posts.id",ondelete="CASCADE")
                     ,nullable=False
                     ,primary_key=True, )