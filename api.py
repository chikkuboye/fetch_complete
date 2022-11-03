import requests
import mysql.connector
import sys
import json
try:
    mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'userdb')
except mysql.connector.Error as e:
    sys.exit('connection failure')
mycursor = mydb.cursor()

data = requests.get("https://jsonplaceholder.typicode.com/todos").text

data_info = json.loads(data)
#print(data_info)

for i in data_info:
    if(i['completed']==False):
        #print(i['completed'])
        id = str(i['userId'])
        complete = str(i['completed'])
        sql = "INSERT INTO `complete`(`User_Id`, `title`, `completed`) VALUES ('"+id+"','"+i['title']+"','"+complete+"')"
        mycursor.execute(sql)
        mydb.commit()
        print('successfully')
    # mycursor.execute(sql)
    # mydb.commit()
    
    