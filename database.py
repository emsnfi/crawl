import mysql.connector
from mysql.connector import errorcode
try:
 cnx = mysql.connector.connect(user='root', password='root',
 host='127.0.0.1', port='8889',
 database='mysql')

except mysql.connector.Error as err:
 if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
 elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exists")
 else:
    print(err)
else:
 cnx.close()
