from ftplib import FTP 

ftp = FTP("ftp.mirror.nl") #ftp.mirror.nl
ftp.login(user="username", passwd="password")
ftp.cwd("ftp://ftp.mirror.nl/")

def grabFile():
	archivo = "archivo.txt"
	localarch = open(archivo, "wb")
	ftp.retrbinary("RETR "+ archivo, localarch.write, 1024)
	ftp.quit()
	localarch.close()

def placeFile():
	archivo = "archivo.txt"
	ftp.storbinary("STOR " + archivo, open(archivo, "rb"))
	ftp.quit()