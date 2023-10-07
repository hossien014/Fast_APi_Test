from pydantic_settings import BaseSettings, SettingsConfigDict


# document: https://docs.pydantic.dev/latest/concepts/pydantic_settings
'''تمام فیلد هایی که در کلاس زیر ساخته می شود به صورت اتوماتیک 
      از انوایرمنت های سیستم فراخوانی میشوند 
'''
class Setting(BaseSettings):
      # این متغییر تنظیمات این کلاس را مشخص می کند مثلا در اینجا بجای فرخوانی از 
      #متغیر های سیستم از فایل که مشخص کردیم فراخوانی می کند
      
      model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

      database_hostname:str
      database_port:str
      database_password:int
      database_name:str
      database_username:str
      secret_key:str
      algorithm:str
      access_token_expire_minute:int 
      SQLALCHEMY_DATABASE_URL :str
  
      # class Config:
      #       env_file = ".env"


setting = Setting()



      


            