import mysql.connector

db = mysql.connector.connect(
  host = "127.0.0.1",
  port="3306",
  user = "root",
  password = "password",
  database="")
  
cur  =  db . cursor ()
cur . execute ( "SELECT * FROM db" )

for  row  in  cur . fetchall ():
    print("123") 
    print ( row [ 0 ])

db . close ()