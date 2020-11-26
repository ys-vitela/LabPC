import yagmail
import json
import argparse

#parser
parser = argparse.ArgumentParser(description = 'Envio de un mensaje a correos listados en un txt')
parser.add_argument('-s', help='Remitente')
parser.add_argument('-d', help='Destinado')
parser.add_argument('-u', help= 'Encabezado del mensaje a enviar')
parser.add_argument('-m', help='Mensaje a enviar a los correos de la lista')
parser.add_argument('-p', help= "Contraseña del remitente")
params = parser.parse_args()

sender = str(params.s)
receiver = str(params.d)
subject = str(params.u)
message = str(params.m)
passwd = str(params.p)

#objeto yag
yag = yagmail.SMTP(user=sender, password=passwd)

contents = 'prueba'

yag.send(to=receiver, subject=subject, contents=contents, attachments=message)