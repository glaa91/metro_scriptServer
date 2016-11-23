#!/usr/bin/python3
import psycopg2
import sys
import os
import subprocess
import datetime
from datetime import datetime
import colorama
from colorama import init
init()

def main():
	from colorama import Fore, Back, Style
	
	print()
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
		print("ERROR DE CONEXION... " + e)
	else:
		conn.set_isolation_level(0)
		cursor = conn.cursor()
		print('CONECTADO')
	
		cursor.execute("""SELECT * FROM v_cuentas;""")
		rows = cursor.fetchall()
		print(Fore.GREEN + "ESTO HAY EN LA VIEW...")
		for row in rows:
			print(Fore.GREEN + "	", row)

		#para comparar el password cifrado con lo ingresado:
		cursor2 = conn.cursor()
		print()
	
		user_s = "gavanses"
		pass_s = "10280"


		cursor2.execute("""SELECT username,password FROM cuentas WHERE username='{user}' AND password='{password}';""".format(user=user_s, password=pass_s))
		rows2=cursor2.fetchall()

		print(Fore.YELLOW + "	ESTO ENCONTRE EN LA BUSQUEDA", str(rows2))
		if str(rows2).find(user_s) != -1:
			print(Fore.MAGENTA + '		USUARIO: {user}'.format(user=user_s))
			if str(rows2).find(pass_s) != -1:
				print(Fore.MAGENTA + '		CLAVE: {password}'.format(password=pass_s))		
		else:
			print(Fore.MAGENTA + '		USUARIO INVALIDO -_-')

#*********************************************************************************************************************

		cursor3 = conn.cursor()
		print()

		cursor3.execute("""SELECT * FROM v_carteles""")
		rows3 = cursor3.fetchall();

		for row3 in rows3:
			print(Fore.YELLOW + row3[0] + " -- " + row3[2])
			hostname_s = row3[2]	
			response = os.system("ping "+ hostname_s + " -c 1")

			#check
			if response==0:
				print(Fore.YELLOW + hostname_s + " UP")
				ping_b = True
			else:
				print(Fore.RED + hostname_s + " DOWN")	
				ping_b = False

			cursor3 = conn.cursor()
			#cursor3.execute("""UPDATE carteles SET pila='3.1' WHERE numeroSerie='00:17:4f:00:00:35';""")
			dateTime_d = datetime.now()
			dateTime_s = dateTime_d.strftime('%y-%m-%d_%H:%M:%S')
			cursor2.execute("""UPDATE carteles SET ping = {pingg} WHERE numeroSerie = '{serie}'""".format(pingg=ping_b,serie=row3[0]))
			update_rows = cursor2.rowcount
			print(Fore.WHITE + str(update_rows) + "-ping")
			cursor2.execute("""UPDATE carteles SET dateTime = '{dateTime}' WHERE numeroSerie = '{serie}'""".format(dateTime=dateTime_s,serie=row3[0]))
			update_rows = cursor2.rowcount
			print(Fore.WHITE + str(update_rows) + "-dateTime")

			conn.commit()
		
	
#		rows4 = cursor3.fetchall();
#		for row4 in rows4:
#			print(Fore.WHITE + row4)

		conn.commit()
		cursor.close()
		cursor2.close()
		cursor3.close()
		conn.close()

		print()
		print()
		print(Fore.RED + '**********************************************************************************************')
		print()
if __name__=="__main__":
	main()
