# وصل کردن به پوستگرس دیتا بیس 

from psycopg2 import connect
from psycopg2._psycopg import cursor
from os import environ
from colorama import Style,Fore
from contextlib import contextmanager

@contextmanager
def get_db()->cursor:
      try:
            conn = connect(
                  database="nfast",
                  user="postgres",
                  password=environ['password'],
                  host="127.0.0.1",
                  port="5432"
                  )

            cursor=conn.cursor()
            print(Fore.GREEN+"Successfuly connect to database"+Style.RESET_ALL)
            yield cursor
      except Exception as exp:      
            print(Fore.RED+"Connetion to database failed!!"+Style.RESET_ALL)
      finally:
            
            cursor.close()
            conn.close()
            print(Fore.GREEN+"Connecion to database closed"+Style.RESET_ALL)
            