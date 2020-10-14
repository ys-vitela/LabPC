#Diego Vitela Herrera 1822993
import socket 
import argparse
from cryptography.fernet import Fernet

#argumentos en command line
description = """ Modo de uso:
		client.py --msj "mensaje a enviar"""

parser = argparse.ArgumentParser(description = 
	"Port scannig", epilog = description, 
	formatter_class = argparse.RawDescriptionHelpFormatter)

parser.add_argument("--msj", metavar = "MSJ", dest = "msj",
	help = "mensaje a enviar", required = True)

params = parser.parse_args()

#generar objeto por cifrar
f = open("clave.key", "wb")
clave = Fernet.generate_key()
f.write(clave)
f.close()

#conversion a bytes
mensaje = params.msj
msj_Bytes = mensaje.encode()

#cifrado
cipher_suite = Fernet(clave)
msj_cifrado = cipher_suite.encrypt(msj_Bytes)
print(f"\nMensaje enviado: {mensaje}")

#dato de coneccion
BUFFER_SIZE = 2048

#coneccion
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1245))

s.send(msj_cifrado)


respuesta = s.recv(BUFFER_SIZE).decode()
print(f"Respuesta recibida: {respuesta}")
s.close()

