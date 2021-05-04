from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import time
import pandas as pd
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode
import ibm_db as idb
import ibm_db_dbi as dbi
import pandas as pd

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'dashdb-txn-sbox-yp-dal09-10.services.dal.bluemix.net'
app.config['MYSQL_USER'] = 'tgz17976'
app.config['MYSQL_PASSWORD'] = '3tc5kj75xb-qnzj9'
app.config['MYSQL_DB'] = 'BLUDB'

def connect():
    global con,conn
    try:
        con=idb.connect("DATABASE=BLUDB;HOSTNAME=dashdb-txn-sbox-yp-dal09-10.services.dal.bluemix.net;PORT=50000;PROTOCOL=TCPIP;UID=tgz17976;PWD=3tc5kj75xb-qnzj9",'','')
        conn = dbi.Connection(con)

    except:
        print("Error in connection, sqlstate = ")
        errorMsg = idb.conn_errormsg()
        print(errorMsg)
connect()

@app.route('/insertDB',methods = ['POST'])
def insertDB():
    stmt = idb.prepare(con, sql_stmt)
    try:
        idb.execute(stmt)
    except:
        print(idb.stmt_errormsg()) 


@app.route('/hi')
def index():
    return "HI NIGGA"



@app.route('/hi2')
def index2():
    return "HI2 NIGGA"



if __name__ == '__main__':
    app.debug = True
    app.run()




