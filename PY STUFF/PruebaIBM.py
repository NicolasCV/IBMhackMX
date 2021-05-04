import time
import pandas as pd
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode
import ibm_db as idb
import ibm_db_dbi as dbi
import pandas as pd

def connect():
    global con,conn
    try:
        con=idb.connect("DATABASE=BLUDB;HOSTNAME=dashdb-txn-sbox-yp-dal09-10.services.dal.bluemix.net;PORT=50000;PROTOCOL=TCPIP;UID=tgz17976;PWD=3tc5kj75xb-qnzj9",'','')
        conn = dbi.Connection(con)

    except:
        print("Error in connection, sqlstate = ")
        errorMsg = idb.conn_errormsg()
        print(errorMsg)

def close():
    global con
    idb.close(con)

def insertDB(sql_stmt):

    connect()
    stmt = idb.prepare(con, sql_stmt)

    try:
        idb.execute(stmt)
    except:
        print(idb.stmt_errormsg())    

    return

def generaClave(valor):
    global conn
    executeOrder = '''
                SELECT IDELECTOR,GENEROID,VOTEID,IDUSADO FROM REGISTROINE
                WHERE CURP = '{curp}';
                '''.format(curp = valor)
    df = pd.read_sql(executeOrder, conn)

    return df

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
    global con, valor

    if(Value == None):
        print('Ya voto')
    else:

        executeOrder = '''
                    UPDATE RegistroIne
                    SET VoteID = '{selector}',
                    GeneroID = '{selector2}'
                    WHERE CURP = '{curp}'
                    '''.format(selector = Value, selector2 = 1 , curp = valor)
        insertDB(executeOrder)

        print("La clave voto se escribio a la base de datos")


def compruebaVoto(claves):
    if((claves.iloc[0,1] == 0) & (claves.iloc[0,2] == None) & (claves.iloc[0,3] == 0)):
        print('Debe generar voto')
        return claves.iloc[0][0]
    else:
        return None

def LeerQr():
    global valor
    img = Image.open('code.png')
    result = decode(img)
    for i in result:
        valor = i.data.decode("utf-8")
    return valor


connect()
escribir(voto(compruebaVoto(generaClave(LeerQr()))))
close()