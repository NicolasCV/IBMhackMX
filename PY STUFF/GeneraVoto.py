import time
import pandas as pd
import sqlite3
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

dbfile = r'C:\Users\David Esquer\Downloads\dbINE.db'
con = sqlite3.connect(dbfile)

def generaClave(valor):
    global con
    cursor = con.cursor()
    executeOrder = '''
                SELECT IDElector,GeneroID,VoteID,IDUsado FROM RegistroIne
                WHERE CURP = "{curp}";
                '''.format(curp = valor)
    cursor.execute(executeOrder)
    claves = cursor.fetchmany()
    print("La Clave de Elector para generar el voto es: ",claves[0][0])
    return claves


def voto(clave):
    global time
    if(clave == None):
        return None
    else:
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


def escribir(Value):
    global con, ingresacurp
    if(Value == None):
        print('este w ya voto')
    else:
        cursor = con.cursor()
        executeOrder = '''
                    UPDATE RegistroIne
                    SET VoteID = "{selector}",
                    GeneroID = "{selector2}"
                    WHERE CURP = "{curp}"
                    '''.format(selector = Value, selector2 = 1 , curp = ingresacurp)
        cursor.execute(executeOrder)
        con.commit()
        print("La clavevoto se escribio a la base de datos")


def compruebaVoto(claves):
    if((claves[0][1] == 0) & (claves[0][2] == None) & (claves[0][3] == 0)):
        print('debe generar voto')
        return claves[0][0]
    else:
        return None

def LeerQr():
    img = Image.open('code.png')
    result = decode(img)
    for i in result:
        valor = i.data.decode("utf-8")
    return valor

escribir(voto(compruebaVoto(generaClave(LeerQr()))))
