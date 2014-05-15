#!/opt/python3/bin/python3
 
import socket
import sys
import os
import time
import socket
import string
import struct
contador=0

	

	
mi_socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def LOGIN():

	
	
	mi_socket_cliente.connect(("192.100.230.21", 21))
	datos_recibidos = mi_socket_cliente.recv(1024) 
	print(datos_recibidos)
	mi_socket_cliente.send(bytes('USER ' + ('userftp\r\n'), 'UTF-8'))
	#il=mi_socket_cliente.sendall(bytes('USER '+'userftp','utf-8'))
	userrev=mi_socket_cliente.recv(1024)
	print(userrev) 
	mi_socket_cliente.send(bytes('PASS '+ ('r3d3sf1s1c@s\r\n'), 'UTF-8'))
	pas=mi_socket_cliente.recv(1024)
	print(pas) 
	 
def LIST_client(dir):
	import os
	try:
		for filename in os.listdir(dir):
			print (filename)
	except:
		print("Directorio inexistente")
def MKD():
	mi_socket_cliente.sendall(bytes('MKD '+'/DESCHAMPS\r\n','utf-8'))
	pas=mi_socket_cliente.recv(1024)
	print(pas)
#def LIST():
	#mi_socket_cliente.sendall(bytes('MKD '+'/FTPPP \r\n','utf-8'))
	#pase=mi_socket_cliente.recv(1024)
	#print(pase)

	
def PWD():
	mi_socket_cliente.sendall(bytes('PWD '+'\r\n','utf-8'))
	pas=mi_socket_cliente.recv(1024) 
	print(pas)
	

 
	
	
def CWD(dir):
	mi_socket_cliente.sendall(bytes('CWD '+dir+'\r\n','utf-8'))
	pas=mi_socket_cliente.recv(1024)
	print(pas)
def LIST(dir):
	if contador ==0:
		mi_socket_cliente1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		mi_socket_cliente1.connect(("192.100.230.21", 21))
		datos_recibidos = mi_socket_cliente1.recv(1024) 
		#print(datos_recibidos)
		mi_socket_cliente1.send(bytes('USER ' + ('userftp\r\n'), 'UTF-8'))
		#il=mi_socket_cliente.sendall(bytes('USER '+'userftp','utf-8'))
		userrev=mi_socket_cliente1.recv(1024)
		#print(userrev) 
		mi_socket_cliente1.send(bytes('PASS '+ ('r3d3sf1s1c@s\r\n'), 'UTF-8'))
		#pas=mi_socket_cliente1.recv(1024)
		#print(pas) 
		mi_socket_cliente1.send(bytes('PASV \r\n','utf-8'))
	#stou=mi_socket_cliente1.recv(1024)
	print (stou)
	stou=stou.decode('utf-8')
	s=stou.partition('(')[2]
	s=s.replace(")","")
	s=s.replace(".","")
	IP1=s.replace(",",".")
	IP=IP1[0:14]
	puertop1=IP1[15:18]
	puertp2=IP1[19:23]
	#print(IP) 
	#print(puertop1)
	#print(puertp2)
	puertopas=(int(puertop1)*256+int(puertp2))
	#print(puertopas)
	mk_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	mk_socket.connect(("192.100.230.21",puertopas))
	mi_socket_cliente1.sendall(bytes('NLST '+dir+'\r\n','utf-8'))
	directorio=mk_socket.recv(1024)
	directorio=str(directorio [:-5])
	directorio=directorio [2:]
	directorio=directorio.split("\\r\\n")
	#directorio=directorio.split(".") 
	#directorio=directorio.split("--")
	#directorio =directorio.partition(",")[1]
	#directorio=directorio.replace (",","\\n")
	print(directorio)
	mi_socket_cliente1.close()
	puertopas=0
	IP=0
	
	
	#portpasivo=a*256+b
	#sock_pasivo=mk_socket(2,hostpasivo,portpasivo)
	#mi_socket_cliente.sendall(bytes('NLIST '+file+'\r\n','utf-8'))
	#directorio=sock_pasivo.recv()
	#print(directorio)
	#file='Python-3.2.tar.bz2'
	#mi_socket_cliente.sendall(bytes('STOR '+file+'\r\n','utf-8'))
	#s2=mi_socket_cliente.recv(1024)
	#print(s2)
#conect()

		#curses.endwin()
		#execute_cmd("df -h") 

def UPLOAD(filename): 
	mi_socket_cliente1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mi_socket_cliente1.connect(("192.100.230.21", 21))
	datos_recibidos = mi_socket_cliente1.recv(1024) 
	#print(datos_recibidos)
	mi_socket_cliente1.send(bytes('USER ' + ('userftp\r\n'), 'UTF-8'))
	#il=mi_socket_cliente.sendall(bytes('USER '+'userftp','utf-8'))
	userrev=mi_socket_cliente1.recv(1024)
	#print(userrev) 
	mi_socket_cliente1.send(bytes('PASS '+ ('r3d3sf1s1c@s\r\n'), 'UTF-8'))
	pas=mi_socket_cliente1.recv(1024)
	#mi_socket_cliente1.send(bytes('TYPE ' + var,'utf-8'))
	#print(pas) 
	#sock_main.send(bytes('STOR '+'README.txt','utf-8'))
	#mi_socket_cliente1.send(bytes('STOR '+fname,'utf-8'))
	var = input("Excribe A o I dependiende de el tipo: ")
	mi_socket_cliente1.send(bytes('TYPE ' + var+'\r\n','utf-8'))
	sto=mi_socket_cliente1.recv(1024)
	print (sto)
	mi_socket_cliente1.send(bytes('PASV \r\n','utf-8'))
	stou=mi_socket_cliente1.recv(1024)
	print (stou)
	stou=stou.decode('utf-8')
	s=stou.partition('(')[2]
	s=s.replace(")","")
	s=s.replace(".","")
	IP1=s.replace(",",".")
	IP=IP1[0:14]
	puertop1=IP1[15:18]
	puertp2=IP1[19:23]
	print(IP) 
	print(puertop1)
	print(puertp2)
	puertopas=(int(puertop1)*256+int(puertp2))
	print(puertopas)
	mk_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#opener = urllib2.build_opener()
	mk_socket.connect(("192.100.230.21",puertopas))
	mi_socket_cliente1.send(bytes('STOR '+filename+ '\r\n','utf-8'))
	
	f = open(filename, 'rb')
	size = os.stat(filename)[6]
	opened = True
	pos = 0
	buff=1024
	
	while opened == True:
		f.seek(pos)
		pos += buff
		if pos >= size:
			piece = f.read(-1)
			opened = False
		else:
			piece = f.read(buff) 
			mk_socket.send(piece)
	mk_socket.close()
	hola=mi_socket_cliente1.recv(1024)
	print(hola)

def DOWNLOAD():
	mi_socket_cliente1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mi_socket_cliente1.connect(("192.100.230.21", 21))
	datos_recibidos = mi_socket_cliente1.recv(1024) 
	#print(datos_recibidos)
	mi_socket_cliente1.send(bytes('USER ' + ('userftp\r\n'), 'UTF-8'))
	#il=mi_socket_cliente.sendall(bytes('USER '+'userftp','utf-8'))
	userrev=mi_socket_cliente1.recv(1024)
	#print(userrev) 
	mi_socket_cliente1.send(bytes('PASS '+ ('r3d3sf1s1c@s\r\n'), 'UTF-8'))
	pas=mi_socket_cliente1.recv(1024)
	#mi_socket_cliente1.send(bytes('TYPE ' + var,'utf-8'))
	#print(pas) 
	#sock_main.send(bytes('STOR '+'README.txt','utf-8'))
	#mi_socket_cliente1.send(bytes('STOR '+fname,'utf-8'))
	var = input("Excribe A o I dependiende de el tipo: ")
	mi_socket_cliente1.send(bytes('TYPE ' + var+'\r\n','utf-8'))
	sto=mi_socket_cliente1.recv(1024)
	print (sto)
	mi_socket_cliente1.send(bytes('PASV \r\n','utf-8'))
	stou=mi_socket_cliente1.recv(1024)
	print (stou)
	stou=stou.decode('utf-8')
	s=stou.partition('(')[2]
	s=s.replace(")","")
	s=s.replace(".","")
	IP1=s.replace(",",".")
	IP=IP1[0:14]
	puertop1=IP1[15:18]
	puertp2=IP1[19:23]
	print(IP) 
	print(puertop1)
	print(puertp2)
	puertopas=(int(puertop1)*256+int(puertp2))
	print(puertopas)
	mk_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#opener = urllib2.build_opener()
	mk_socket.connect(("192.100.230.21",puertopas))
	mi_socket_cliente1.send(bytes('RETR '+ 'index.html\r\n','utf-8'))
	l='A'
	f = open('index.html', 'wb')
	size=size = os.stat('index.html')[6]
	print(size)
	while l != "":
		l=mk_socket.recv(size)
		l=l.decode()
		f.write(l)
	f.close()		
	hola=mi_socket_cliente1.recv(1024)
	print(hola)
	
variable=0
	#mi_socket_cliente.storbinary('STOR '+'pokebola2.png', f) 
LOGIN()
while variable != 8 :
	print("Please enter a number...")
	print("1 - Ver y navegar directorio Local ")
	print("2 - Ver y navegar directorio Remote ")
	print("3 - Enviar Archivos")
	print( "4 - Descargar archivos")
	print("5 - Cambiar permisos")
	print("6 - Renombrar archivo")
	print("7 - Eliminar Archivo")
	print( "8 - EXIT")
	variable=int(input("Selecciona una opcion"))
	if variable ==1:
		
		Dir=input("Escriba el Directorio para mostrar ")
		LIST_client(Dir)
		input("Press enter")
	if variable ==2:
		
		Dir=input("Escriba el Directorio para mostrar ")
		LIST(Dir)
		var=0
		while var !=2:
			var=int(input("desea cambiar de directorio \n 1 Si \n 2 no"))
			Dir2=input("Escriba el Directorio para mostrar ")
			CWD(Dir2)
			LIST(Dir2)
			
		
		input("Press enter")
	if variable ==3:
		
		Dir=input("Escriba nombre de Archivo  ")
		UPLOAD(Dir)
	if variable ==4:
		
		Dir=input("Escriba nombre de Archivo  ")
		DOWNLOAD()
		
	if variable ==5:
		fn=input("Nombre del archivo")
		Per=input("Permisos P.e. 777")
		mi_socket_cliente.send(bytes('SITE CHMOD '+Per+' '+fn+' \r\n','utf-8'))
		stou=mi_socket_cliente.recv(1024)
		print (stou)
	if variable ==6:
		fn=input("Nombre del archivo")
		Per=input("Nombre nuevo")
		mi_socket_cliente.send(bytes('RNFR '+fn+'\r\n','utf-8'))
		stou=mi_socket_cliente.recv(1024)
		print (stou)
		mi_socket_cliente.send(bytes('RNTO '+Per+'\r\n','utf-8'))
		sto=mi_socket_cliente.recv(1024)
		print (sto)
	if variable==7:
		fn=input("Nombre del archivo")
		try:
			mi_socket_cliente.send(bytes('DELE '+fn+'\r\n','utf-8'))
			stou=mi_socket_cliente.recv(1024)
			print (stou)
		except:
			mi_socket_cliente.send(bytes('RMD '+fn+'\r\n','utf-8'))
			sto=mi_socket_cliente.recv(1024)
			print (sto)