#!/usr/bin/python3
import psycopg2
import sys
import os
import subprocess
#from loggerInit import *
import html
import urllib.request, urllib.error
#from scriptPsql import *
from scriptFunciones import *
import datetime
from datetime import datetime
import colorama
from colorama import init
init()

# DEBUG: Detailed information, typically of interest only when diagnosing problems.
	#logging.debug('DEBUG') --> YELLOW
# INFO: Confirmation that things are working as expected.
	#logging.info(Fore.WHITE + Back.BLACK + 'INFO')
# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
	#logging.warning(Fore.GREEN + Back.RED + 'WARNING')
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
	#logging.error(Fore.MAGENTA + Back.CYAN + 'ERROR')
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
	#logging.critical(Fore.BLACK + Back.MAGENTA + 'CRITICAL')

#def main():
from colorama import Fore, Back, Style
#logging.basicConfig(filename='scriptRuning.log', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#INICIO LA FUNCION LOGGIN PARA QUE EL LOG ME TOME ARCHIVOS Y CONSOLA
init_logger()

dateTime_d = datetime.now()
dateTime_s = dateTime_d.strftime('%y-%m-%d_%H:%M:%S')
logging.info(Fore.RED + Back.BLACK + '**********************************************************************************************' + Fore.WHITE)
logging.info(Fore.WHITE + 'INICIANDO SCRIPT... 		ver. 2016.11.30' + Fore.WHITE)

#
#	SE OPTIMIZO EL CODIGO, AHORA NO SE REPITEN LINEAS QUE HACEN LO MISMO, EN LA PARTE DE ESCRIBIR LA TABLAS. AHORA ESTA ESCRITO UNA SOLA VEZ
#	FUNCIONA CORECTAMENTE LA OPCION DE CARGAR UN NUEVO CARTEL, Y QUE LA MAC NO ESTE EN LA TABLA carteles
#	SE CORRIGIO EL MENSAJE warning Y error, EL COLOR DE FONDO.
#	SE AGREGARON MENSAJES DE info PARA CUANDO SE AGREGA UN NUEVO CARTEL.
#	SE MEJORO LOS COLORES Y FONDO DE LAS ALERTAS.
#

#define String conection
connection_s = "host='localhost' dbname='scp' user='postgres' password='postgres'"
#print conction string to database
logging.debug(Fore.CYAN + 'Connecting to database -> {conector}'.format(conector=connection_s) + Fore.WHITE)

#***********************************************************ejemplo para comparar nombre de usuario y contrasena*********************************************************
try:
	conn = psycopg2.connect(connection_s)
except psycopg2.OperationalError as e:
	logging.critical(Back.MAGENTA + Fore.BLACK + "ERROR DE CONEXION A LA BASE DE DATOS... " + str(e) + Back.BLACK + Fore.WHITE)
else:
	conn.set_isolation_level(0)
	cursor = conn.cursor()
	cursor2 = conn.cursor()
	cursor3 = conn.cursor()
	cursor4 = conn.cursor()
	logging.info(Fore.WHITE + 'CONECTADO' + Fore.WHITE)
	logging.debug(Fore.CYAN + Back.BLACK + "ME PUDE CONECTAR A LA BASE DE DATOS!" + Fore.WHITE)
	cursor3.execute("""SELECT * FROM v_estaciones;""")
	rows3 = cursor3.fetchall();
	databaseMac = 'null'
	for row3 in rows3:
		logging.debug(Fore.CYAN + "" + Fore.WHITE)
		logging.debug(Fore.CYAN + "******************************************")
		logging.info(Fore.WHITE + "" + Fore.WHITE)
		logging.info(Fore.WHITE + "numeroSerie:" + row3[0] + " -- numeroCartel:" + row3[1] + " -- ip:" + row3[2] + Fore.WHITE)
		dbEstacionesMac_s = row3[0]
		dbEstacionesIp_s = row3[2]
		dbEstacionesNumeroCartel_s = row3[1]
		logging.debug(Fore.CYAN + "ESTA ES LA MAC QUE ENCONTRE EN LA TABLA ESTACIONES:" + dbEstacionesMac_s + Fore.WHITE)
		logging.debug(Fore.CYAN + "ESTA ES LA IP QUE ENCONTRE EN LA TABLA ESTACIONES:" + dbEstacionesIp_s + Fore.WHITE)
		htmlWebIp_s="http://" + dbEstacionesIp_s + "/runtime.shtml"
		logging.debug(Fore.CYAN + "ESTA ES LA DIRECCION A LA QUE ME VOY A TRATAR DE CONECTAR " + htmlWebIp_s + Fore.WHITE)
		dateTime_d = datetime.now()
		dateTime_s = dateTime_d.strftime('%y-%m-%d_%H:%M:%S')
		logging.debug(Fore.CYAN + "ESTA ES LA HORA QUE VOY A CARGAR EN LA TABLA " + dateTime_s + Fore.WHITE)
		response = os.system("ping "+ dbEstacionesIp_s + " -c 1 -W 1")
		#check
		if response==0:
			logging.info(Fore.WHITE + dbEstacionesIp_s + " UP" + Fore.WHITE)
			logging.debug(Fore.CYAN + Back.BLACK + "EL PING DIO OK, ALGO ME RESPONDIO" + Fore.WHITE)
			ping_b = True
		else:
			logging.warning(Back.RED + Fore.GREEN + dbEstacionesIp_s + " DOWN" + Back.BLACK + Fore.WHITE)
			logging.debug(Fore.CYAN + Back.BLACK + "EL PING DIO MAL, NO ME RESPONDIO" + Fore.WHITE)
			ping_b = False
		#actualizo el ping en la tabla estaciones
		cursor2.execute("""UPDATE estaciones SET ping = {pingg} WHERE numeroCartel = '{cartel}'""".format(pingg=ping_b,cartel=dbEstacionesNumeroCartel_s))
		update_rows = cursor2.rowcount
		#imprimo el resultado de la actualizacion
		if update_rows==1:
			logging.info(Fore.WHITE + "UPDATE OK -- " +str(update_rows) + "-ping" + Fore.WHITE)
			logging.debug(Fore.CYAN + Back.BLACK + "ACTUALIZE BIEN EL PING" + Fore.WHITE)
		else:
			logging.error(Fore.MAGENTA +Back.CYAN + "UPDATE ERROR -- " +str(update_rows) + "-ping" + Fore.WHITE)
			logging.debug(Fore.CYAN + Back.BLACK + "NO ACTUALIZE BIEN EL PING" + Fore.WHITE)
		#actualizo el datetime en la tabla estaciones
		cursor2.execute("""UPDATE estaciones SET dateTime = '{dateTime}' WHERE numeroCartel = '{cartel}'""".format(dateTime=dateTime_s,cartel=dbEstacionesNumeroCartel_s))
		update_rows = cursor2.rowcount
		#imprimo el resultado de la actualizacion
		if update_rows==1:
			logging.info(Fore.WHITE + Back.BLACK + "UPDATE OK -- " + str(update_rows) + "-dateTime" + Fore.WHITE)
			logging.debug(Fore.CYAN + Back.BLACK + "ACTUALIZE BIEN EL DATETIME" + Fore.WHITE)
		else:
			logging.error(Fore.MAGENTA + Back.CYAN + "UPDATE ERROR -- " + str(update_rows) + "-dateTime" + Fore.WHITE)
			logging.debug(Fore.CYAN + Back.BLACK + "NO ACTUALIZE BIEN EL DATETIME" + Fore.WHITE)
		conn.commit()
		htmlTemp_s = 'null'
		htmlFuente5v_s = 'null'
		htmlFuente24v_s = 'null'
		htmlFuentePpic_s = 'null'
		htmlFuente5pic_s = 'null'
		htmlCorriente_s = 'null'
		htmlMac_s = 'null'
		htmlMensaje_s = 'null'
		if ping_b==True:
			#si el ping dio OK, hay algo que responde => voy a buscar los datos en la pagina
			try:
				f = urllib.request.urlopen(htmlWebIp_s)
			except urllib.error.HTTPError as e:
				logging.error(Fore.MAGENTA + Back.CYAN + "HTTP ERROR... CODE:" + str(f.getcode()) + Fore.WHITE +  Back.BLACK)
			except urllib.error.URLError as e:
				logging.error(Fore.MAGENTA + Back.CYAN + "URL ERROR... CODE:"+ str(e) + Fore.WHITE + Back.BLACK)
			else:
				#si estoy aca es porque la pagina existe y me pude conectar
				logging.debug(Fore.CYAN + Back.BLACK + "EXISTE LA PAGINA DEL MICRO, ME PUDE CONECTAR, Y AHORA LA VOY A LEER" + Fore.WHITE)
				#200
				#ACA DEBO OBTENER EL MAC ADRESS Y VER SI ES NULL EN LA TABLA ESTACIONES
				#	SI EN NULL DEBO BUSCAR UNO NUEVO EN LA TABLA CARTELES.
				#	SI NO ES NULL, LO TENGO QUE COMPRAR Y VER QUE SEA EL MISMO.
				#		SI ES IGUAL OK.
				#		SI ES DISTINTO CARGO EL NUEVO.
				logging.info(Fore.WHITE + Back.BLACK + "HTTP: OK... CODE:" + str(f.getcode()) + Fore.WHITE)
				pageString_s = str(f.read())
				#ASI VOY A BUSCAR LOS INCIOS DE LOS MENSAJES A SACAR DE LA PAGINA
				startTemp_s = "Temperatura ="
				startFuente5v_s = "Fuente 5 volt = "
				startFuente24v_s = "Fuente 24 Volt Semaforos = "
				startFuentePpic_s = "Estado PPIC = "
				startFuente5pic_s = "Fuente Display 5 volt = "
				startCorriente_s = "Corriente = "
				startMac_s = "MAC = "
				startPila_s = "Pila = "
				startMensaje_s = "Mensaje = "
				endTemp_s = "&#"
				end_s = "\\r\\n"
				endMensaje_s = "</pre>"
				#LEO TODO EL CONTENIDO
				logging.debug(Fore.CYAN + "ESTE ES EL CONTENIDO QUE ENCONTRE EN EL HTML: " + pageString_s + Fore.WHITE)
				#LEO TEMPERATURA
				htmlTemp_s = find_string(pageString_s, startTemp_s, endTemp_s)
				logging.debug(Fore.CYAN + "HTML TEMP:" + htmlTemp_s + Fore.WHITE)
				#LEO FUENTE 5v
				htmlFuente5v_s = find_string(pageString_s, startFuente5v_s, end_s)
				logging.debug(Fore.CYAN + "HTML FUENTE 5v:" + htmlFuente5v_s + Fore.WHITE)
				#LEO FUENTE 24v
				htmlFuente24v_s = find_string(pageString_s, startFuente24v_s, end_s)
				logging.debug(Fore.CYAN + "HTML FUENTE 24v:" + htmlFuente24v_s + Fore.WHITE)
				#LEO FUENTE PPIC
				htmlFuentePpic_s = find_string(pageString_s, startFuentePpic_s, end_s)
				logging.debug(Fore.CYAN + "HTML FUENTE PPIC:" + htmlFuentePpic_s + Fore.WHITE)
				#LEO FUENTE 5PIC
				htmlFuente5pic_s = find_string(pageString_s, startFuente5pic_s, end_s)
				logging.debug(Fore.CYAN + "HTML FUENTE 5PIC:" + htmlFuente5pic_s + Fore.WHITE)
				#LEO CORRIENTE
				htmlCorriente_s = find_string(pageString_s, startCorriente_s, end_s)
				logging.debug(Fore.CYAN + "HTML CORRIENTE:" + htmlCorriente_s + Fore.WHITE)
				#LEO PILA
				htmlPila_s = find_string(pageString_s, startPila_s, end_s)
				logging.debug(Fore.CYAN + "HTML PILA:" + htmlPila_s + Fore.WHITE)
				#LEO MAC -- IMPORTANTE!
				htmlMac_s = find_string(pageString_s, startMac_s, end_s)
				logging.debug(Fore.CYAN + "HTML MAC:" + htmlMac_s + Fore.WHITE)
				#LEO MENSAJE
				htmlMensaje_s = find_string(pageString_s, startMensaje_s, endMensaje_s)
				logging.debug(Fore.CYAN + "HTML MENSAJE:" + htmlMensaje_s + Fore.WHITE)

				#AHORA QUE TENGO LA MAC, PRIMERO DEBO COMPARARLA CON LA QUE ENCONTRE EN LA TABLA
				if htmlMac_s==dbEstacionesMac_s:
					#LA MAC DE LA TABLA ESTACION ES IGUAL A LA DE LA PAGINA => EL CARTEL QUE ESTA EN LA ESTACION ES EL QUE DICE LA BASE DE DATOS!
					logging.debug(Fore.CYAN + "htmlMac==dbEstacionesMac => LA TABLA estaciones ESTA ACTUALIZADA!" + Fore.WHITE)
					logging.info(Fore.WHITE + "htmlMac==dbEstacionesMac => LA TABLA estaciones ESTA ACTUALIZADA!" + Fore.WHITE)
					#INFO
					#OJO!!!!! SI MAGIACAMENTE EL CARTEL SE BORRO, DEBERIA VERIFICARLO!
					#
					#
					macUpdate_s = htmlMac_s;
				else:
					#LA MAC DE LA TABLA ESTACIONES ES DISTINTA A LA DE LA PAGINA
					#BUSCAR EN LA TABLA CARTELES LA htmlMac, EN CASO DE QUE NO EXISTA, AGREGO LA NUEVA MAC
					logging.debug(Fore.CYAN + "htmlMac!=dbEstacionesMac => LA TABLA estaciones NO ESTA ACTUALIZADA..." + Fore.WHITE)
					logging.info(Fore.WHITE + "htmlMac!=dbEstacionesMac => LA TABLA estaciones NO ESTA ACTUALIZADA..." + Fore.WHITE)
					#cursor4 = conn.cursor()
					cursor4.execute("""SELECT * FROM v_carteles;""")
					rows4 = cursor4.fetchall();
					dbCartelesMac_s = 'null'
					dbCartelesMac_b = False		#VARIABLE PARA SABER SI LA MAC YA ESTA EN LA LISTA DE carteles
					for row4 in rows4:	#BUSCO LA MAC EN LA TABLA carteles
						dbCartelesMac_s = str(row4[0])
						#logging.debug(Fore.CYAN + "ESTO ENCONTRE dbEstacionesMac => " + dbCartelesMac_s + Fore.WHITE)
						if dbCartelesMac_s==htmlMac_s:
							dbCartelesMac_b = True
							#logging.info(Fore.WHITE + "MAC ENCONTRADA: " + dbCartelesMac_s + Fore.WHITE)
							logging.debug(Fore.CYAN + Back.BLACK + "ENCONTRE LA mac: " + str(dbCartelesMac_s) + Fore.WHITE)
							macUpdate_s = dbCartelesMac_s;
							#ENCONTRE LA MAC DEL HTML EN LA TABLA DE CARTELES
							#AHORA TENGO QUE ACTUALIZAR LA TABLA DE ESTACIONES CON LA NUEVA MAC!
							estado_b = update_psql(conn, "estaciones", "numeroSerie", macUpdate_s, "numeroCartel", dbEstacionesNumeroCartel_s)
							logging.debug(Fore.CYAN + Back.BLACK + "mac ACTUALIZADO EN TABLA estaciones? -> UPDATE: " + str(estado_b) + "- numeroSerie" + Fore.WHITE)
							logging.info(Fore.WHITE + "mac ACTUALIZADA EN TABLA estaciones? --> UPDATE: " +str(estado_b) + " - numeroSerie" + Fore.WHITE)

					if dbCartelesMac_b == False:
						#logging.info(Fore.WHITE + "MAC ENCONTRADA: " + dbCartelesMac_s + Fore.WHITE)
						logging.debug(Fore.CYAN + Back.BLACK + "NO ENCONTRE LA mac... LA TENGO QUE AGREGAR A TABLA carteles! " + Fore.WHITE)
						macUpdate_s = htmlMac_s;
						#NO ENCONTRE LA MAC... DEBO AGREGARLA						
						estado_b=insert_psql(conn, "carteles", "'{serie}','{tiempo}','{pila}','{temp}','{corri}','{fuente5}','{fuente24}','{fuenteP}','{fuente5p}','msj'".format(serie=htmlMac_s, tiempo=dateTime_s, pila=htmlPila_s, temp=htmlTemp_s, corri=htmlCorriente_s, fuente5=htmlFuente5v_s, fuente24=htmlFuente24v_s, fuenteP=htmlFuentePpic_s, fuente5p=htmlFuente5pic_s, msj=htmlMensaje_s))
						logging.debug(Fore.CYAN + Back.BLACK + "mac INSERTADA? -> " + str(estado_b) + Fore.WHITE)
						if estado_b == True:
							estado_b = update_psql(conn, "estaciones", "numeroSerie", htmlMac_s, "numeroCartel", dbEstacionesNumeroCartel_s)
							logging.debug(Fore.CYAN + Back.BLACK + "NUEVA mac ACTUALIZADO EN TABLA estaciones? -> UPDATE: " + str(estado_b) + "- numeroSerie" + Fore.WHITE)
							logging.info(Fore.WHITE + Back.BLACK + "NUEVA mac ACTUALIZADO EN TABLA estaciones? -> UPDATE: " + str(estado_b) + "- numeroSerie" + Fore.WHITE)

				#TENGO QUE ACTUALIZAR TODOS LOS PARAMETROS DEL CARTEL AHORA EN LA TABLA carteles -- VARIABLE macUpdate
				logging.info(Fore.WHITE + "ACTUALIZANDO TABLA estaciones... " + Fore.WHITE)
				logging.debug(Fore.CYAN + "AHORA VOY A ACTUALIZAR LA TABLA estaciones CON TODOS LOS DATOS..." + Fore.WHITE)
				#DATTIME				
				estado_b = update_psql(conn, "carteles", "dateTime", dateTime_s, "numeroSerie", macUpdate_s)
				logging.info(Fore.WHITE + "UPDATE " + str(estado_b) + " - dateTime" + Fore.WHITE)
				logging.debug(Fore.CYAN + Back.BLACK + "dateTime ACTUALIZADO? -> " + str(estado_b) + Fore.WHITE)
				#PILA
				estado_b = update_psql(conn, "carteles", "pila", htmlPila_s, "numeroSerie", macUpdate_s)
				logging.info(Fore.WHITE + "UPDATE " + str(estado_b) + " - pila" + Fore.WHITE)
				logging.debug(Fore.CYAN + Back.BLACK + "pila ACTUALIZADO? -> " + str(estado_b) + Fore.WHITE)
				#TEMPERATURA
				estado_b = update_psql(conn, "carteles", "temp", htmlTemp_s, "numeroSerie", macUpdate_s)
				logging.info(Fore.WHITE + "UPDATE " + str(estado_b) + " - temperatura" + Fore.WHITE)
				logging.debug(Fore.CYAN + Back.BLACK + "temperatura ACTUALIZADO? -> " + str(estado_b) + Fore.WHITE)
				#CORRIENTE
				estado_b = update_psql(conn, "carteles", "corriente", htmlCorriente_s, "numeroSerie", macUpdate_s)
				logging.info(Fore.WHITE + "UPDATE " + str(estado_b) + " - corriente" + Fore.WHITE)
				logging.debug(Fore.CYAN + Back.BLACK + "corriente ACTUALIZADA? -> " + str(estado_b) + Fore.WHITE)
				#FUENTE5V
				estado_b = update_psql(conn, "carteles", "fuente5v", htmlFuente5v_s, "numeroSerie", macUpdate_s)
				logging.info(Fore.WHITE + "UPDATE " + str(estado_b) + " - fuente5v" + Fore.WHITE)
				logging.debug(Fore.CYAN + Back.BLACK + "fuente5v ACTUALIZADO? -> " + str(estado_b) + Fore.WHITE)
				#fuente24V
				estado_b = update_psql(conn, "carteles", "fuente24v", htmlFuente24v_s, "numeroSerie", macUpdate_s)
				logging.info(Fore.WHITE + "UPDATE " + str(estado_b) + " - fuente24v" + Fore.WHITE)
				logging.debug(Fore.CYAN + Back.BLACK + "fuente24v ACTUALIZADO? -> " + str(estado_b) + Fore.WHITE)
				#FUENTEPPIC
				estado_b = update_psql(conn, "carteles", "fuentePpic", htmlFuentePpic_s, "numeroSerie", macUpdate_s)
				logging.info(Fore.WHITE + "UPDATE " + str(estado_b) + " - fuenteppic" + Fore.WHITE)
				logging.debug(Fore.CYAN + Back.BLACK + "fuenteppic ACTUALIZADO? -> "+ str(estado_b) + Fore.WHITE)
				#FUENTE5PIC
				estado_b = update_psql(conn, "carteles", "fuente5pic", htmlFuente5pic_s, "numeroSerie", macUpdate_s)
				logging.info(Fore.WHITE + "UPDATE " + str(estado_b) + " - fuente5pic" + Fore.WHITE)
				logging.debug(Fore.CYAN + Back.BLACK + "fuente5pic ACTUALIZADO? -> " + str(estado_b) + Fore.WHITE)
				#MENSAJE
				estado_b = update_psql(conn, "carteles", "mensaje", htmlMensaje_s, "numeroSerie", macUpdate_s)
				logging.info(Fore.WHITE + "UPDATE " + str(estado_b) + " - mensaje" + Fore.WHITE)
				logging.debug(Fore.CYAN + Back.BLACK + "mensaje ACTUALIZADO? -> " + str(estado_b) + Fore.WHITE)
				conn.commit()

	#estado_binsert_psql(conn, "carteles", "'{serie}','{tiempo}','{pila}','{temp}','{corri}','{fuente5}','{fuente24}','{fuenteP}','fuente5p','msj'".format(serie=htmlMac_s, tiempo=dateTime_s, pila=htmlPila_s, temp=htmlTemp_s, corri=htmlCorriente_s, fuente5=htmlFuente5v_s, fuente24=htmlFuente24v_s, fuentep=htmlFuentePpic_s, fuente5p=htmlFuente5pic, msj=htmlMensaje_s))

	conn.commit()
	cursor.close()
	cursor2.close()
	cursor3.close()
	conn.close()
logging.info("" + Fore.WHITE)
logging.info(Fore.RED + Back.BLACK + '**********************************************************************************************' + Fore.WHITE)
#if __name__=="__main__":
#	main()
