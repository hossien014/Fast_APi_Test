from fastapi import FastAPI , Depends,HTTPException
from .orm_db import schemas   
from .routers import users,auth,post,vote
from .orm_db.database import base , engine
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated 

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

''' دستور زیر باعث میشود با هر بار استارت برنامه کل مدل های دیتا بیس در صورت
عدم وجود ساخته بشوند 
'''
# base.metadata.create_all(bind=engine)


'''cros policy : https://fastapi.tiangolo.com/tutorial/cors/
   مشخص می کند که چه دامنه هایی اجازه استفاده از ای پی ای ما را دارند 
'''
# origins=['https://www.google.com','http://www.masaf.ir'] مثال
origins=["*"]
app.add_middleware(
    CORSMiddleware, # تایپ میدل ورد
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



#روتر ها ها مانند بلوپرینت ها در فلسک هستند
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(post.router)
app.include_router(vote.router)

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
