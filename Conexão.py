import mysql.connector

con = mysql.connector.connect(host='localhost',database='dados',user='root',password='root')

if con.is_connected():
    db_info = con.get_server_info()
    print("conenctado, ",db_info)
    cursor = con.cursor()
    cursor.execute("SELECT DATABASE();")
    linha = cursor.fetchone()
    print("banco de dados ",linha)
    
if con.is_connected():
    cursor.close()
    con.close()
    print("Desconectado")    