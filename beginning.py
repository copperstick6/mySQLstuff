import keys
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
connection = pymysql.connect(host='localhost',
                             user='copperstick6',
                             password=keys.sqlKey(),
                             db= "menu",
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    result = cursor.fetchall()
    for record in result:
        print("id: " + str(record['id']) + " email: " + str(record['email']) + " password: " + str(record['password']))

connection.close()
