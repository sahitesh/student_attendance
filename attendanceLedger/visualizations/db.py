import mysql.connector as connector

def GetTableData(request):
    con = mysql.connector.connect(user='root', password='1234',host='127.0.0.1',port='3306',database='Vaagdevi')
    sql = "SELECT * FROM {}".format(request['tableName'])
    cursor = con.cursor()
    cursor = cursor.execute(sql)
    for record in cursor:
        print(record)
    return cursor