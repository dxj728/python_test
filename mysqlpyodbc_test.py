import pyodbc
import mysql.connector


# cnxn =pyodbc.connect("DRIVER={MySQL ODBC 5.3 Unicode Driver};SERVER=120.78.218.216;PORT=3306;DATABASE=coralcloud;USER=root;PASSWODD=123456;OPTION=3")
# cursor = cnxn.cursor()
# cursor.execute("select uid, displayname, password from oc_users")
# row = cursor.fetchall()
# for i in row:
#     print(i)

##---------------------------------------------------OK------------------------------------------------------
conn = mysql.connector.connect(host='120.78.218.216', database='coralcloud', user='root', password='123456')
cursor = conn.cursor()
cursor.execute("select uid, displayname, password from oc_users")
row = cursor.fetchall()
for i in row:
    print(i)



