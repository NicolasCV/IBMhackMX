import sqlite3
import time
import mysql.connector

idp = 1  #se generara el voto de este id

import MySQLdb

db = MySQLdb.connect(host='192.168.0.136',  # your host name is often 'localhost'
                     user='root',            
                     passwd='password',  
                     db='INE_Checkin') 

#"XCM76348"."REGISTRO"
dbfile = r'C:\Users\David Esquer\Downloads\dbINE.db'
#con = sqlite3.connect(dbfile)

def generaClave(idp):
    global con
    executeOrder = '''
                SELECT IDElector FROM Registro
                WHERE ID = "{idd}";
                '''.format(idd = idp)
    stmt = ibm_db.exec_immediate(con, executeOrder)
    claves = ibm_db.execute(stmt)
    claves = cursor.fetchmany()
    print("La Clave de Elector para generar el voto es: ",claves[0][0])
    return claves[0][0]

def probando():
    return 1

def voto(clave):
    global time
    clave2 = clave[0:6]
    numeros1 = [ord(character) for character in clave2]
    num1 = [str(i) for i in numeros1]
    res1 = int("".join(num1))
    t = time.localtime()
    current_time = time.strftime("%H%M%S", t)
    time = int(current_time[0:2]) + 64
    time2 = (int(current_time[2:4]))+64
    time3 = (int(current_time[4:]))+64
    res3 = chr(int(clave[12:14]) + 64)
    chartime = chr(time)
    chartime2 = chr(time2)
    chartime3 = chr(time3)

    clavevoto = str(chartime) + str(res1) + str(chartime2) + str(res3) + str(chartime3)
    print("La Clave de voto generada es: ",clavevoto)
    return clavevoto

def escribir(Value, idp):
    global con
    cursor = con.cursor()
    executeOrder = '''
                UPDATE Registro
                SET VoteID = "{selector}",
                GeneroID = "{selector2}"
                WHERE ID = "{idd}";
                '''.format(selector = Value, selector2 = 1 , idd = idp)
    cursor.execute(executeOrder)
    con.commit()
    print("La clavevoto se escribio a la base de datos")

#claves = generaClave(idp)
#escribir(voto(claves), idp)
