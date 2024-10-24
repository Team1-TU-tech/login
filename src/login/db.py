import pymysql.cursors
import os

def get_conn():
    conn = pymysql.connect(host=os.getenv("DB", "127.0.0.1"),
                            user='login_user',
                            password='login_passwd',
                            database='login',
                            port=int(os.getenv("DB_PORT", "6033")),
                            cursorclass=pymysql.cursors.DictCursor)

    return conn
