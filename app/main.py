from fastapi import FastAPI , Depends,HTTPException
from .orm_db import schemas   
from .routers import users,auth
from .orm_db.database import base , engine
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated 

app = FastAPI()

base.metadata.create_all(bind=engine)

#روتر ها ها مانند بلوپرینت ها در فلسک هستند
app.include_router(users.router)
app.include_router(auth.router)


@app.get('/', response_model=schemas.simpleRespones)
def root():
    return {"respones": [{"server runing on ": 127}]}




# oauth2_schema=OAuth2PasswordBearer(tokenUrl="token")


# @app.post("/token")
# async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
#     print("hossien")
#     return{"access_token":"mohamd rasoll allh" ,"token_type":"bearer"}


# @app.get("/t")
# # annotated به یک متغیر توضیحات اضافه می کند مثلا در مورد زیر 
# # متغیر توکن یک استرینگ است 
# #قبل از شروع فانکشن ابتدا چک  فانکشنی که در دیپندنسی وارد شده است اجرا می شود اگر اجرا شدادامه می دهد
# def token(token:Annotated[str,Depends(oauth2_schema)]):
#     return {"token " : token}
