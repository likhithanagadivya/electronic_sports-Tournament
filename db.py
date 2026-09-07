from pymysql import connect

def get_connection():
    connection = connect(
    host="localhost" ,
    user="root",
    password="Likhitha@1234",
    database="electronic_sports"
    )
    return connection