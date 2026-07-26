import os
import pymysql
from dotenv import load_dotenv

# Update this path if your .env is elsewhere
load_dotenv('/home/ubuntu/.env')

def create_database():
    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_port = int(os.getenv("DB_PORT", "3306"))
    db_name = os.getenv("DB_NAME")

    print(f"Connecting to: {db_host}:{db_port}")

    connection = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        port=db_port
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`;")
            connection.commit()

        print(f"Database '{db_name}' created successfully or already exists ✅")

    finally:
        connection.close()

if __name__ == "__main__":
    create_database()