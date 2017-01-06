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
    sql = "INSERT INTO users (id, email, password) VALUES (%s, %s, %s);"
    cursor.execute(sql, ("4", "testing@testing.com", "Kappa"))
    connection.commit()
    getData = "SELECT * FROM users"
    cursor.execute(getData)
    result = cursor.fetchall()
    for record in result:
        print("id: " + str(record['id']) + " email: " + str(record['email']) + " password: " + str(record['password']))

connection.close()
