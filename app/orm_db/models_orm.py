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