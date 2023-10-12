from jose import JWTError,jwt
from datetime import datetime ,timedelta
from fastapi import HTTPException ,status,Depends
from fastapi.security import OAuth2PasswordBearer
from .orm_db import schemas,database,models_orm
from sqlalchemy.orm import Session
from . import config

ALGORITHM=config.setting.algorithm
M_SECRET_KEY=config.setting.secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=config.setting.access_token_expire_minute 

'''این خط کد چند کار را به عهده دارد
اول اینکه در صفحه داک قابلیت لاگین را اضافه میکند 
و وقتی یوزر نیم و پسورد را وارد میکنید ان را به اند پوینتی که به عنوان ارگومان 
میفرستید ارسال و توکن را دریافت میکند.
و به غیر از صفحه داک خود این فانکشن را به عنوان وابستگی میتوان به فانکشن های دیگر اعمال کرد
'''
oauth_schema= OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data:dict):
      
      to_encode =data.copy()
      expir=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
      to_encode.update({"exp":expir})
      encode_jwt=jwt.encode(to_encode,M_SECRET_KEY,algorithm=ALGORITHM)
      return encode_jwt
      
      

def verify_token(token_ ,credentials_error):
      try:
            payload:dict=jwt.decode(token_,M_SECRET_KEY,algorithms=[ALGORITHM])
            userid:str=payload.get("user_id")
            if userid is None:
                  raise credentials_error
            else: 
                  toekn_data=schemas.TokenData(id=userid)
      except JWTError :
            raise credentials_error
      
      return toekn_data      
      
def get_currnt_user(token:str=Depends(oauth_schema) ,db:Session=Depends(database.get_db)) :
      
      credentials_error=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                      detail="Could not validate credentials !!",
                                      headers={"WWW-Authenticate": "Bearer"})
      
      token_data:schemas.TokenData = verify_token(token,credentials_error)
      user =db.query(models_orm.user_db).filter(models_orm.user_db.id==token_data.id).first()
      return user
      
      