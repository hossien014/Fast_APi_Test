
from fastapi import APIRouter,HTTPException,status,Depends
from sqlalchemy.orm import Session
from..orm_db.database import get_db
from..orm_db import schemas
from..orm_db.models_orm import user_db
from passlib.context import CryptContext
from .. import oauth2
from fastapi.security import OAuth2PasswordRequestForm 

pw_content= CryptContext(schemes="bcrypt",deprecated="auto") # برای وریفای کردن هش 

router=APIRouter(tags=["authentication"],prefix="/login")

@router.post("/",status_code=status.HTTP_202_ACCEPTED)
#کردنتشال باید از نوع  او آث باشد که  یعنی باید یک فیلد به اسم یوزر نیم و یک فیلد پسورد دارد و 
#حتما باید از نوع فرم باشد
def login(credentials:OAuth2PasswordRequestForm=Depends() ,db:Session=Depends(get_db)):
      user_in_database=db.query(user_db).filter(user_db.username==credentials.username).first()
      if not user_in_database:
            raise HTTPException(status_code=status.HTTP_402_PAYMENT_REQUIRED,detail="invalid credentials ")
      
      hash_pass=user_in_database.password
      if pw_content.verify(credentials.password,hash_pass) is False :
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail="Invaild credentials!")
      
      jwt_token=oauth2.create_access_token(data={"user_id":user_in_database.id}) 
      return {"access_token":jwt_token,"token_type":"bearer"}
      