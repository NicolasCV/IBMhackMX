import pyqrcode

ClaveElector = ""

def generaQr(Clave):
    qrCode = pyqrcode.create(Clave, error='L', version=27, mode='binary')
    qrCode.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
    qrCode.show()


generaQr(ClaveElector)