import pymysql

import os
from dotenv import load_dotenv
load_dotenv('/home/jenkins/.env')

def create_database():
    connection=pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        name=os.getenv("DB_NAME"),
        password=os.getenv("DB_PASSWORD"),
        port=int(os.getenv("DB_PORT",3306))
    )
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXIST {os.getenv("DB_NAME")};")
            connection.commit()
            print(f"database : {os.getenv("DB_NAME")} is create or exixts✅")
    except ExceptionGroup as e:
        print("error :" ,e)
        
    finally:
        connection.close()
        
if __name__=="__main__":
    create_database()        
                    