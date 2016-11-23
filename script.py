#!/usr/bin/python3
import psycopg2
import sys
import os
import subprocess
#import lxml
import html
import urllib.request, urllib.error
import datetime
from datetime import datetime
import colorama
from colorama import init
init()

#def main():
from colorama import Fore, Back, Style
	
print()
print("ver. 2016.11.21")
print(Back.WHITE + Fore.RED + '**********************************************************************************************')
dateTime_d = datetime.now()
dateTime_s = dateTime_d.strftime('%y-%m-%d_%H:%M:%S')
print(Style. BRIGHT + Back.MAGENTA + Fore.CYAN + dateTime_s)
print(Back.MAGENTA + Fore.BLUE + 'INICIANDO SCRIPT...')
print(Back.BLACK)

#define String conection    
connection_s = "host='201.235.196.210' dbname='scp' user='postgres' password='postgres' "

#print conction string to database
print(Fore.WHITE + 'Connecting to database -> {conector}'.format(conector=connection_s))
	
#***********************************************************ejemplo para comparar nombre de usuario y contrasena*********************************************************
try:	
	conn = psycopg2.connect(connection_s)
except psycopg2.OperationalError as e:
	print("ERROR DE CONEXION... " + str(e))
else:
	conn.set_isolation_level(0)
	cursor = conn.cursor()
	cursor2 = conn.cursor()
	cursor3 = conn.cursor()
	print('CONECTADO')
	print()

	cursor3.execute("""SELECT * FROM v_estaciones""")
	rows3 = cursor3.fetchall();
	
	for row3 in rows3:
		print(Fore.YELLOW + "numeroSerie:" + row3[0] + " -- numeroCartel:" + row3[1] + " -- ip:" + row3[2])
		hostname_s = row3[2]
		hostnameHtml_s="http://" + hostname_s + "/runtime.shtml"
		print(hostnameHtml_s)
		dateTime_d = datetime.now()
		dateTime_s = dateTime_d.strftime('%y-%m-%d_%H:%M:%S')
		print(Fore.WHITE + dateTime_s)
		response = os.system("ping "+ hostname_s + " -c 1 -W 1")
		#check
		if response==0:
			print(Fore.YELLOW + hostname_s + " UP")
			ping_b = True
			#buscar el mac adress y compararlo con la tabla.
			#	si coincide sigo normalmente actualizando todo.
			#	si no coincide, 1 borrarlo. 2 comparar este numero en la tabla carteles, si se ecuentra, lo escribo y sigo
		else:
			print(Fore.RED + hostname_s + " DOWN")	
			ping_b = False
			#escribo false y sigo	
		cursor2.execute("""UPDATE estaciones SET ping = {pingg} WHERE numeroCartel = '{cartel}'""".format(pingg=ping_b,cartel=row3[1]))
		update_rows = cursor2.rowcount
		print(Fore.WHITE + str(update_rows) + "-ping")
		cursor2.execute("""UPDATE estaciones SET dateTime = '{dateTime}' WHERE numeroCartel = '{cartel}'""".format(dateTime=dateTime_s,cartel=row3[1]))
		update_rows = cursor2.rowcount
		print(Fore.WHITE + str(update_rows) + "-dateTime")
		conn.commit()
		htmlTemp_s = 'null'
		htmlFuente5v_s = 'null'
		htmlFuente24v_s = 'null'
		htmlFuentePpic_s = 'null'
		htmlFuente5pic_s = 'null'
		htmlMensaje_s = 'null'
		if ping_b==True:
			try:
				f = urllib.request.urlopen(hostnameHtml_s)
			except urllib.error.HTTPError as e:
				print("HTTP ERRORR... CODE:" + str(f.getcode()))
			except urllib.error.URLError as e:
				print("URl ERROR... CODE:"+ str(e))
			else:
				#200
				print("OK... CODE:" + str(f.getcode()))
				pageString_s = str(f.read())
				startTemp_s = "Temperatura ="
				startFuente5v_s = "Fuente 5 volt = "
				startFuente24v_s = "Fuente 24 Volt Semaforos = "
				startFuentePpic_s = "Estado PPIC = "
				startFuente5pic_s = "Fuente Display 5 volt = "
				startMensaje_s = "Mensaje = "
				endTemp_s = "&#"
				end_s = " \\r\\n"
				endMensaje_s = "$</pre>"
				#CONTENIDO
				print("CONTENT: " + pageString_s)

				#TEMPERATURA
				startTemp = pageString_s.find(startTemp_s)+len(startTemp_s)
				endTemp = pageString_s.find(endTemp_s,startTemp)
				htmlTemp_s = pageString[startTemp:endTemp]

				#FUENTE 5v
				startFuente5v = pageString_s.find(startFuente5v_s)+len(startFuente5v_s)
				endFuente5v = pageString_s.find(end_s,startFuente5v)
				htmlFuente5v_s = pageString_s[startFuente5v:endFuente5v]

				#FUENTE 24v
				startFuente24v = pageString_s.find(startFuente24v_s)+len(startFuente24v_s)
				endFuente24v = pageString_s.find(end_s,startFuente24v)
				htmlFuente24v_s = pageString_s[startFuente24v:endFuente24v]

				#FUENTE PPIC
				startFuentePpic = pageString_s.find(startFuentePpic_s)+len(startFuentePpic_s)
				endFuentePpic = pageString_s.find(end_s,startFuentePpic)
				htmlFuentePpic_s = pageString_s[startFuentePpic:endFuentePpic]

				#FUENTE 5PIC
				startFuente5pic = pageString_s.find(startFuente5pic_s)+len(startFuente5pic_s)
				endFuente5pic = pageString_s.find(end_s,startFuente5pic)
				htmlFuente5pic_s = pageString_s[startFuente5pic:endFuente5pic]

				#MENSAJE
				startMensaje = pageString_s.find(startMensaje_s)+len(startMensaje_s)
				endMensaje = pageString_s.find(endMensaje_s,startMensaje)
				htmlMensaje_s = pageString_s[startMensaje:endMensaje]

		else:
			print(Fore.RED + "PING FALSE...")
		print(Fore.YELLOW + "TEMP:" + htmlTemp_s)
		print("FUENTE 5v:" + htmlFuente5v_s)
		print("FUENTE 24v:" + htmlFuente24v_s)
		print("FUENTE PPIC:" + htmlFuentePpic_s)				
		print("FUENTE 5PIC:" + htmlFuente5pic_s)
		print("MENSAJE:" + htmlMensaje_s)				
		print()
		print()
conn.commit()
cursor.close()
cursor2.close()
cursor3.close()
conn.close()
print()
print()
print(Fore.RED + '**********************************************************************************************')
print()
#if __name__=="__main__":
#	main()
