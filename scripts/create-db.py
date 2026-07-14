import os
import pymysql
from dotenv import load_dotenv

load_dotenv('/home/jenkins/.env')


def create_database():
    connection = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=int(os.getenv("DB_PORT", 3306))
    )

    try:
        with connection.cursor() as cursor:
            db_name = os.getenv("DB_NAME")

            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {'DB_NAME'};")
            connection.commit()

            print(f"Database {'DB_NAME'} created successfully or already exists ✅✅")

    except Exception as e:
        print("Error:", e)

    finally:
        connection.close()


if __name__ == "__main__":
    create_database()