#!/usr/bin/python3
import psycopg2
import sys
import os
import subprocess
from loggerInit import *
#import lxml
import html
import urllib.request, urllib.error
import datetime
from datetime import datetime
import colorama
from colorama import init
init()

# DEBUG: Detailed information, typically of interest only when diagnosing problems.
	#logging.debug('DEBUG') --> YELLOW
# INFO: Confirmation that things are working as expected.
	#logging.info('INFO') --> WHITE
# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
	#logging.warning('WARNING')
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
	#logging.error('ERROR')
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
	#logging.critical('CRITICAL')

#def main():
from colorama import Fore, Back, Style
#logging.basicConfig(filename='scriptRuning.log', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
init_logger()

dateTime_d = datetime.now()
dateTime_s = dateTime_d.strftime('%y-%m-%d_%H:%M:%S')
logging.info(Fore.RED + Back.BLACK + '**********************************************************************************************' + Fore.WHITE)
logging.info(Fore.WHITE + 'INICIANDO SCRIPT... 		ver. 2016.11.23' + Fore.WHITE)

#define String conection
connection_s = "host='localhost' dbname='scp' user='postgres' password='postgres'"
#print conction string to database
logging.debug(Fore.CYAN + 'Connecting to database -> {conector}'.format(conector=connection_s) + Fore.WHITE)

#***********************************************************ejemplo para comparar nombre de usuario y contrasena*********************************************************
try:
	conn = psycopg2.connect(connection_s)
except psycopg2.OperationalError as e:
	logging.critical(Fore.RED + "ERROR DE CONEXION... " + str(e) + Fore.WHITE)
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
			logging.warning(Fore.MAGENTA + dbEstacionesIp_s + " DOWN" + Fore.WHITE)
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
				#ASI VOY A BUSCAR LOS INCIOS DE LOS MESAES A SACAR DE LA PAGINA
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
				startTemp = pageString_s.find(startTemp_s)+len(startTemp_s)
				endTemp = pageString_s.find(endTemp_s,startTemp)
				htmlTemp_s = pageString_s[startTemp:endTemp]
				logging.debug(Fore.CYAN + "HTML TEMP:" + htmlTemp_s + Fore.WHITE)

				#LEO FUENTE 5v
				startFuente5v = pageString_s.find(startFuente5v_s)+len(startFuente5v_s)
				endFuente5v = pageString_s.find(end_s,startFuente5v)
				htmlFuente5v_s = pageString_s[startFuente5v:endFuente5v]
				logging.debug(Fore.CYAN + "HTML FUENTE 5v:" + htmlFuente5v_s + Fore.WHITE)

				#LEO FUENTE 24v
				startFuente24v = pageString_s.find(startFuente24v_s)+len(startFuente24v_s)
				endFuente24v = pageString_s.find(end_s,startFuente24v)
				htmlFuente24v_s = pageString_s[startFuente24v:endFuente24v]
				logging.debug(Fore.CYAN + "HTML FUENTE 24v:" + htmlFuente24v_s + Fore.WHITE)

				#LEO FUENTE PPIC
				startFuentePpic = pageString_s.find(startFuentePpic_s)+len(startFuentePpic_s)
				endFuentePpic = pageString_s.find(end_s,startFuentePpic)
				htmlFuentePpic_s = pageString_s[startFuentePpic:endFuentePpic]
				logging.debug(Fore.CYAN + "HTML FUENTE PPIC:" + htmlFuentePpic_s + Fore.WHITE)

				#LEO FUENTE 5PIC
				startFuente5pic = pageString_s.find(startFuente5pic_s)+len(startFuente5pic_s)
				endFuente5pic = pageString_s.find(end_s,startFuente5pic)
				htmlFuente5pic_s = pageString_s[startFuente5pic:endFuente5pic]
				logging.debug(Fore.CYAN + "HTML FUENTE 5PIC:" + htmlFuente5pic_s + Fore.WHITE)

				#LEO CORRIENTE
				startCorriente = pageString_s.find(startCorriente_s)+len(startCorriente_s)
				endCorriente = pageString_s.find(end_s,startCorriente)
				htmlCorriente_s = pageString_s[startCorriente:endCorriente]
				logging.debug(Fore.CYAN + "HTML CORRIENTE:" + htmlCorriente_s + Fore.WHITE)

				#LEO PILA
				startPila = pageString_s.find(startPila_s)+len(startPila_s)
				endPila = pageString_s.find(end_s,startPila)
				htmlPila_s = pageString_s[startPila:endPila]
				logging.debug(Fore.CYAN + "HTML PILA:" + htmlPila_s + Fore.WHITE)

				#LEO MAC -- IMPORTANTE!
				startMac = pageString_s.find(startMac_s)+len(startMac_s)
				endMac = pageString_s.find(end_s,startMac)
				htmlMac_s = pageString_s[startMac:endMac]
				logging.debug(Fore.CYAN + "HTML MAC:" + htmlMac_s + Fore.WHITE)

				#LEO MENSAJE
				startMensaje = pageString_s.find(startMensaje_s)+len(startMensaje_s)
				endMensaje = pageString_s.find(endMensaje_s,startMensaje)
				htmlMensaje_s = pageString_s[startMensaje:endMensaje]
				logging.debug(Fore.CYAN + "HTML MENSAJE:" + htmlMensaje_s + Fore.WHITE)

				#AHORA QUE TENGO LA MAC, PRIMERO DEBO COMPARARLA CON LA QUE ENCONTRE EN LA TABLA
				if htmlMac_s==dbEstacionesMac_s:
					#LA MAC DE LA TABLA ESTACION ES IGUAL A LA DE LA PAGINA => EL CARTEL QUE ESTA EN LA ESTACION ES EL QUE DICE LA BASE DE DATOS!
					logging.debug(Fore.CYAN + "htmlMac==dbEstacionesMac => LA TABLA ESTACIONES ESTA ACTUALIZADA!" + Fore.WHITE)
					#DATETIME
					cursor4.execute("""UPDATE carteles SET dateTime = '{dateTime}' WHERE numeroSerie = '{numeroSerie}'""".format(dateTime=dateTime_s,numeroSerie=dbEstacionesMac_s))
					update_rows4 = cursor4.rowcount
					if update_rows4==1:
						logging.info(Fore.WHITE + "UPDATE OK -- " +str(update_rows4) + "-dateTime" + Fore.WHITE)
						logging.debug(Fore.CYAN + Back.BLACK + "ACTUALIZE BIEN dateTime A LA TABLA CARTELES" + Fore.WHITE)
					else:
						logging.error(Fore.MAGENTA +Back.CYAN + "UPDATE ERROR -- " +str(update_rows4) + "-dateTime" + Fore.WHITE)
						logging.debug(Fore.CYAN + Back.BLACK + "NO ACTUALIZE BIEN dateTime A CARTELES" + Fore.WHITE)

					#PILA
					cursor4.execute("""UPDATE carteles SET pila = '{pila}' WHERE numeroSerie = '{numeroSerie}'""".format(pila=htmlPila_s,numeroSerie=dbEstacionesMac_s))
					update_rows4 = cursor4.rowcount
					if update_rows4==1:
						logging.info(Fore.WHITE + "UPDATE OK -- " +str(update_rows4) + "-pila" + Fore.WHITE)
						logging.debug(Fore.CYAN + Back.BLACK + "ACTUALIZE BIEN pila A LA TABLA CARTELES" + Fore.WHITE)
					else:
						logging.error(Fore.MAGENTA +Back.CYAN + "UPDATE ERROR -- " +str(update_rows4) + "-pila" + Fore.WHITE)
						logging.debug(Fore.CYAN + Back.BLACK + "NO ACTUALIZE BIEN pila A CARTELES" + Fore.WHITE)					
					#TEMPERATURA
					cursor4.execute("""UPDATE carteles SET temp = '{temperatura}' WHERE numeroSerie = '{numeroSerie}'""".format(temperatura=htmlTemp_s,numeroSerie=dbEstacionesMac_s))
					update_rows4 = cursor4.rowcount
					if update_rows4==1:
						logging.info(Fore.WHITE + "UPDATE OK -- " +str(update_rows4) + "-temperatura" + Fore.WHITE)
						logging.debug(Fore.CYAN + Back.BLACK + "ACTUALIZE BIEN temperatura A LA TABLA CARTELES" + Fore.WHITE)
					else:
						logging.error(Fore.MAGENTA +Back.CYAN + "UPDATE ERROR -- " +str(update_rows4) + "-temperatura" + Fore.WHITE)
						logging.debug(Fore.CYAN + Back.BLACK + "NO ACTUALIZE BIEN temperatura A CARTELES" + Fore.WHITE)
					#CORRIENTE
					cursor4.execute("""UPDATE carteles SET corriente = '{corriente}' WHERE numeroSerie = '{numeroSerie}'""".format(corriente=htmlCorriente_s,numeroSerie=dbEstacionesMac_s))
					update_rows4 = cursor4.rowcount
					if update_rows4==1:
						logging.info(Fore.WHITE + "UPDATE OK -- " +str(update_rows4) + "-corriente" + Fore.WHITE)
						logging.debug(Fore.CYAN + Back.BLACK + "ACTUALIZE BIEN corriente A LA TABLA CARTELES" + Fore.WHITE)
					else:
						logging.error(Fore.MAGENTA +Back.CYAN + "UPDATE ERROR -- " +str(update_rows4) + "-corriente" + Fore.WHITE)
						logging.debug(Fore.CYAN + Back.BLACK + "NO ACTUALIZE BIEN corriente A CARTELES" + Fore.WHITE)
					#FUENTE5V
					cursor4.execute("""UPDATE carteles SET fuente5v = '{fuente5v}' WHERE numeroSerie = '{numeroSerie}'""".format(fuente5v=htmlFuente5v_s,numeroSerie=dbEstacionesMac_s))
					update_rows4 = cursor4.rowcount
					if update_rows4==1:
						logging.info(Fore.WHITE + "UPDATE OK -- " +str(update_rows4) + "-fuente5v" + Fore.WHITE)
						logging.debug(Fore.CYAN + Back.BLACK + "ACTUALIZE BIEN fuente5v A LA TABLA CARTELES" + Fore.WHITE)
					else:
						logging.error(Fore.MAGENTA +Back.CYAN + "UPDATE ERROR -- " +str(update_rows4) + "-fuente5v" + Fore.WHITE)
						logging.debug(Fore.CYAN + Back.BLACK + "NO ACTUALIZE BIEN fuente5v A CARTELES" + Fore.WHITE)
					#fuente24V
					cursor4.execute("""UPDATE carteles SET fuente24v = '{fuente24v}' WHERE numeroSerie = '{numeroSerie}'""".format(fuente24v=htmlFuente24v_s,numeroSerie=dbEstacionesMac_s))
					update_rows4 = cursor4.rowcount
					if update_rows4==1:
						logging.info(Fore.WHITE + "UPDATE OK -- " +str(update_rows4) + "-fuente24v" + Fore.WHITE)
						logging.debug(Fore.CYAN + Back.BLACK + "ACTUALIZE BIEN fuente24v A LA TABLA CARTELES" + Fore.WHITE)
					else:
						logging.error(Fore.MAGENTA +Back.CYAN + "UPDATE ERROR -- " +str(update_rows4) + "-fuente24v" + Fore.WHITE)
						logging.debug(Fore.CYAN + Back.BLACK + "NO ACTUALIZE BIEN fuente24v A CARTELES" + Fore.WHITE)
					#FUENTEPPIC
					cursor4.execute("""UPDATE carteles SET fuentePpic = '{fuentePpic}' WHERE numeroSerie = '{numeroSerie}'""".format(fuentePpic=htmlFuentePpic_s,numeroSerie=dbEstacionesMac_s))
					update_rows4 = cursor4.rowcount
					if update_rows4==1:
						logging.info(Fore.WHITE + "UPDATE OK -- " +str(update_rows4) + "-fuenteppic" + Fore.WHITE)
						logging.debug(Fore.CYAN + Back.BLACK + "ACTUALIZE BIEN fuenteppic A LA TABLA CARTELES" + Fore.WHITE)
					else:
						logging.error(Fore.MAGENTA +Back.CYAN + "UPDATE ERROR -- " +str(update_rows4) + "-fuenteppic" + Fore.WHITE)
						logging.debug(Fore.CYAN + Back.BLACK + "NO ACTUALIZE BIEN fuenteppic A CARTELES" + Fore.WHITE)
					#FUENTE5PIC
					cursor4.execute("""UPDATE carteles SET fuente5pic = '{fuente5pic}' WHERE numeroSerie = '{numeroSerie}'""".format(fuente5pic=htmlFuente5pic_s,numeroSerie=dbEstacionesMac_s))
					update_rows4 = cursor4.rowcount
					if update_rows4==1:
						logging.info(Fore.WHITE + "UPDATE OK -- " +str(update_rows4) + "-fuente5pic" + Fore.WHITE)
						logging.debug(Fore.CYAN + Back.BLACK + "ACTUALIZE BIEN fuente5pic A LA TABLA CARTELES" + Fore.WHITE)
					else:
						logging.error(Fore.MAGENTA +Back.CYAN + "UPDATE ERROR -- " +str(update_rows4) + "-fuente5pic" + Fore.WHITE)
						logging.debug(Fore.CYAN + Back.BLACK + "NO ACTUALIZE BIEN fuente5pic A CARTELES" + Fore.WHITE)
					#MENSAJE
					cursor4.execute("""UPDATE carteles SET mensaje = '{msj}' WHERE numeroSerie = '{numeroSerie}'""".format(msj=htmlMensaje_s,numeroSerie=dbEstacionesMac_s))
					update_rows4 = cursor4.rowcount
					if update_rows4==1:
						logging.info(Fore.WHITE + "UPDATE OK -- " +str(update_rows4) + "-mensaje" + Fore.WHITE)
						logging.debug(Fore.CYAN + Back.BLACK + "ACTUALIZE BIEN mensaje A LA TABLA CARTELES" + Fore.WHITE)
					else:
						logging.error(Fore.MAGENTA +Back.CYAN + "UPDATE ERROR -- " +str(update_rows4) + "-mensaje" + Fore.WHITE)
						logging.debug(Fore.CYAN + Back.BLACK + "NO ACTUALIZE BIEN mensaje A CARTELES" + Fore.WHITE)
					conn.commit()
				else:
					#LA MAC DE LA TABLA ESTACIONES ES DISTINTA A LA DE LA PAGINA
					#BUSCAR EN LA TABLA CARTELES LA htmlMac
					logging.debug(Fore.CYAN + "htmlMac!=dbEstacionesMac => LA TABLA ESTACIONES NO ESTA ACTUALIZADA..." + Fore.WHITE)
					#cursor4 = conn.cursor()
					cursor4.execute("""SELECT * FROM v_carteles;""")
					rows4 = cursor4.fetchall();
					dbCartelesMac_s = 'null'
					for row4 in rows4:
						dbCartelesMac_s = str(row4[0])
						#logging.debug(Fore.CYAN + "ESTO ENCONTRE dbEstacionesMac => " + dbCartelesMac_s + Fore.WHITE)
						if dbCartelesMac_s==htmlMac_s:
							logging.info(Fore.WHITE + "MAC ECNOTRADA: " + dbCartelesMac_s + Fore.WHITE)
							#ENCONTRE LA MAC DEL HTML EN LA TABLA DE CARTELES
							#AHORA TENGO QUE ACTUALIZAR LA TABLA DE ESTACIONES CON LA NUEVA MAC!
							logging.debug(Fore.CYAN + "ENCONTRE LA MAC EN LA TABLA CARTELES!" + dbCartelesMac_s + Fore.WHITE)
							cursor4.execute("""UPDATE estaciones SET numeroSerie = '{numeroSerie}' WHERE numeroCartel = '{cartel}'""".format(numeroSerie=dbCartelesMac_s,cartel=dbEstacionesNumeroCartel_s))
							update_rows4 = cursor4.rowcount
							#imprimo el resultado de la actualizacion
							if update_rows4==1:
								logging.info(Fore.WHITE + "UPDATE OK -- " +str(update_rows4) + "-numeroSerie" + Fore.WHITE)
								logging.debug(Fore.CYAN + Back.BLACK + "ACTUALIZE BIEN LA NUEVA Mac A LA TABLA ESTACIONES" + Fore.WHITE)
							else:
								logging.error(Fore.MAGENTA +Back.CYAN + "UPDATE ERROR -- " +str(update_rows4) + "-numeroSerie" + Fore.WHITE)
								logging.debug(Fore.CYAN + Back.BLACK + "NO ACTUALIZE BIEN LA NUEVA Mac A ESTACIONES" + Fore.WHITE)
							#TENGO QUE ACTUALIZAR TODOS LOS PARAMETROS DEL CARTEL AHORA EN LA TABLA CARTELES
							#DATETIME
							cursor4.execute("""UPDATE carteles SET dateTime = '{dateTime}' WHERE numeroSerie = '{numeroSerie}'""".format(dateTime=dateTime_s,numeroSerie=dbCartelesMac_s))
							update_rows4 = cursor4.rowcount
							if update_rows4==1:
								logging.info(Fore.WHITE + "UPDATE OK -- " +str(update_rows4) + "-dateTime" + Fore.WHITE)
								logging.debug(Fore.CYAN + Back.BLACK + "ACTUALIZE BIEN dateTime A LA TABLA CARTELES" + Fore.WHITE)
							else:
								logging.error(Fore.MAGENTA +Back.CYAN + "UPDATE ERROR -- " +str(update_rows4) + "-dateTime" + Fore.WHITE)
								logging.debug(Fore.CYAN + Back.BLACK + "NO ACTUALIZE BIEN dateTime A CARTELES" + Fore.WHITE)
							#PILA
							cursor4.execute("""UPDATE carteles SET pila = '{pila}' WHERE numeroSerie = '{numeroSerie}'""".format(pila=htmlPila_s,numeroSerie=dbCartelesMac_s))
							update_rows4 = cursor4.rowcount
							if update_rows4==1:
								logging.info(Fore.WHITE + "UPDATE OK -- " +str(update_rows4) + "-pila" + Fore.WHITE)
								logging.debug(Fore.CYAN + Back.BLACK + "ACTUALIZE BIEN pila A LA TABLA CARTELES" + Fore.WHITE)
							else:
								logging.error(Fore.MAGENTA +Back.CYAN + "UPDATE ERROR -- " +str(update_rows4) + "-pila" + Fore.WHITE)
								logging.debug(Fore.CYAN + Back.BLACK + "NO ACTUALIZE BIEN pila A CARTELES" + Fore.WHITE)
							#TEMPERATURA
							cursor4.execute("""UPDATE carteles SET temp = '{temperatura}' WHERE numeroSerie = '{numeroSerie}'""".format(temperatura=htmlTemp_s,numeroSerie=dbCartelesMac_s))
							update_rows4 = cursor4.rowcount
							if update_rows4==1:
								logging.info(Fore.WHITE + "UPDATE OK -- " +str(update_rows4) + "-temperatura" + Fore.WHITE)
								logging.debug(Fore.CYAN + Back.BLACK + "ACTUALIZE BIEN temperatura A LA TABLA CARTELES" + Fore.WHITE)
							else:
								logging.error(Fore.MAGENTA +Back.CYAN + "UPDATE ERROR -- " +str(update_rows4) + "-temperatura" + Fore.WHITE)
								logging.debug(Fore.CYAN + Back.BLACK + "NO ACTUALIZE BIEN temperatura A CARTELES" + Fore.WHITE)
							#CORRIENTE
							cursor4.execute("""UPDATE carteles SET corriente = '{corriente}' WHERE numeroSerie = '{numeroSerie}'""".format(corriente=htmlCorriente_s,numeroSerie=dbCartelesMac_s))
							update_rows4 = cursor4.rowcount
							if update_rows4==1:
								logging.info(Fore.WHITE + "UPDATE OK -- " +str(update_rows4) + "-corriente" + Fore.WHITE)
								logging.debug(Fore.CYAN + Back.BLACK + "ACTUALIZE BIEN corriente A LA TABLA CARTELES" + Fore.WHITE)
							else:
								logging.error(Fore.MAGENTA +Back.CYAN + "UPDATE ERROR -- " +str(update_rows4) + "-corriente" + Fore.WHITE)
								logging.debug(Fore.CYAN + Back.BLACK + "NO ACTUALIZE BIEN corriente A CARTELES" + Fore.WHITE)
							#FUENTE5V
							cursor4.execute("""UPDATE carteles SET fuente5v = '{fuente5v}' WHERE numeroSerie = '{numeroSerie}'""".format(fuente5v=htmlFuente5v_s,numeroSerie=dbCartelesMac_s))
							update_rows4 = cursor4.rowcount
							if update_rows4==1:
								logging.info(Fore.WHITE + "UPDATE OK -- " +str(update_rows4) + "-fuente5v" + Fore.WHITE)
								logging.debug(Fore.CYAN + Back.BLACK + "ACTUALIZE BIEN fuente5v A LA TABLA CARTELES" + Fore.WHITE)
							else:
								logging.error(Fore.MAGENTA +Back.CYAN + "UPDATE ERROR -- " +str(update_rows4) + "-fuente5v" + Fore.WHITE)
								logging.debug(Fore.CYAN + Back.BLACK + "NO ACTUALIZE BIEN fuente5v A CARTELES" + Fore.WHITE)
							#fuente24V
							cursor4.execute("""UPDATE carteles SET fuente24v = '{fuente24v}' WHERE numeroSerie = '{numeroSerie}'""".format(fuente24v=htmlFuente24v_s,numeroSerie=dbCartelesMac_s))
							update_rows4 = cursor4.rowcount
							if update_rows4==1:
								logging.info(Fore.WHITE + "UPDATE OK -- " +str(update_rows4) + "-fuente24v" + Fore.WHITE)
								logging.debug(Fore.CYAN + Back.BLACK + "ACTUALIZE BIEN fuente24v A LA TABLA CARTELES" + Fore.WHITE)
							else:
								logging.error(Fore.MAGENTA +Back.CYAN + "UPDATE ERROR -- " +str(update_rows4) + "-fuente24v" + Fore.WHITE)
							logging.debug(Fore.CYAN + Back.BLACK + "NO ACTUALIZE BIEN fuente24v A CARTELES" + Fore.WHITE)
							#FUENTEPPIC
							cursor4.execute("""UPDATE carteles SET fuenteppic = '{fuenteppic}' WHERE numeroSerie = '{numeroSerie}'""".format(fuenteppic=htmlFuentePpic_s,numeroSerie=dbCartelesMac_s))
							if update_rows4==1:
								logging.info(Fore.WHITE + "UPDATE OK -- " +str(update_rows4) + "-fuenteppic" + Fore.WHITE)
								logging.debug(Fore.CYAN + Back.BLACK + "ACTUALIZE BIEN fuenteppic A LA TABLA CARTELES" + Fore.WHITE)
							else:
								logging.error(Fore.MAGENTA +Back.CYAN + "UPDATE ERROR -- " +str(update_rows4) + "-fuenteppic" + Fore.WHITE)
								logging.debug(Fore.CYAN + Back.BLACK + "NO ACTUALIZE BIEN fuenteppic A CARTELES" + Fore.WHITE)
							#FUENTE5PIC
							cursor4.execute("""UPDATE carteles SET fuente5pic = '{fuente5pic}' WHERE numeroSerie = '{numeroSerie}'""".format(fuente5pic=htmlFuente5pic_s,numeroSerie=dbCartelesMac_s))
							update_rows4 = cursor4.rowcount
							if update_rows4==1:
								logging.info(Fore.WHITE + "UPDATE OK -- " +str(update_rows4) + "-fuente5pic" + Fore.WHITE)
								logging.debug(Fore.CYAN + Back.BLACK + "ACTUALIZE BIEN fuente5pic A LA TABLA CARTELES" + Fore.WHITE)
							else:
								logging.error(Fore.MAGENTA +Back.CYAN + "UPDATE ERROR -- " +str(update_rows4) + "-fuente5pic" + Fore.WHITE)
								logging.debug(Fore.CYAN + Back.BLACK + "NO ACTUALIZE BIEN fuente5pic A CARTELES" + Fore.WHITE)
							#MENSAJE
							cursor4.execute("""UPDATE carteles SET mensaje = '{msj}' WHERE numeroSerie = '{numeroSerie}'""".format(msj=htmlMensaje_s,numeroSerie=dbCartelesMac_s))
							update_rows4 = cursor4.rowcount
							if update_rows4==1:
								logging.info(Fore.WHITE + "UPDATE OK -- " +str(update_rows4) + "-mensaje" + Fore.WHITE)
								logging.debug(Fore.CYAN + Back.BLACK + "ACTUALIZE BIEN mensaje A LA TABLA CARTELES" + Fore.WHITE)
							else:
								logging.error(Fore.MAGENTA +Back.CYAN + "UPDATE ERROR -- " +str(update_rows4) + "-mensaje" + Fore.WHITE)
								logging.debug(Fore.CYAN + Back.BLACK + "NO ACTUALIZE BIEN mensaje A CARTELES" + Fore.WHITE)

							conn.commit()
		#else:
		#	print(Fore.RED + "PING FALSE...")
			#SI EL PING ES FALSO, YA LO INDIQUE ARRIBA Y ACA NO DEBERIA HACER NADA
		logging.info(Fore.WHITE + "TEMP:" + htmlTemp_s + Fore.WHITE)
		logging.info(Fore.WHITE + "FUENTE 5v:" + htmlFuente5v_s + Fore.WHITE)
		logging.info(Fore.WHITE + "FUENTE 24v:" + htmlFuente24v_s + Fore.WHITE)
		logging.info(Fore.WHITE + "FUENTE PPIC:" + htmlFuentePpic_s + Fore.WHITE)				
		logging.info(Fore.WHITE + "FUENTE 5PIC:" + htmlFuente5pic_s + Fore.WHITE)
		logging.info(Fore.WHITE + "CORRIENTE:" + htmlCorriente_s + Fore.WHITE)
		logging.info(Fore.WHITE + "MAC:" + htmlMac_s + Fore.WHITE)
		logging.info(Fore.WHITE + "MENSAJE:" + htmlMensaje_s + Fore.WHITE)
		logging.debug(Fore.CYAN + "******************************************" + Fore.WHITE)
conn.commit()
cursor.close()
cursor2.close()
cursor3.close()
conn.close()
logging.info("" + Fore.WHITE)
logging.info(Fore.RED + Back.BLACK + '**********************************************************************************************' + Fore.WHITE)
#if __name__=="__main__":
#	main()
