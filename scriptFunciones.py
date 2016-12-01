import psycopg2
import os
import logging

#FUNCION PARA ACTUALIZAR LA TABLA DE LA BASE DE DATOS
def update_psql(conn, db, var_set1, var_set2, var_where1, var_where2):
	estado_b = False
	cursor = conn.cursor()
	cursor.execute("""UPDATE {dataBase} SET {var_s1} = '{var_s2}' WHERE {var_w1} = '{var_w2}'""".format(dataBase=db, var_s1=var_set1, var_s2=var_set2 , var_w1=var_where1, var_w2=var_where2))
	update_rows = cursor.rowcount
	if update_rows==1:
		estado_b = True
	else:
		estado_b = False
	conn.commit()
	return estado_b

#FUNCION PARA AGREGAR DATOS A UNA TABLA DE LA BASE DE DATOS
def insert_psql(conn, db, datos_s):
	estado_b = False
	cursor = conn.cursor()
	cursor.execute("""INSERT INTO {dataBase} VALUES({d1});""".format(dataBase=db, d1=datos_s))
	update_rows = cursor.rowcount
	if update_rows==1:
		estado_b = True
	else:
		estado_b = False
#	conn.commmit()
	return estado_b

#FUNCION PARA SACAR LOS STRING DEL LA PAGINA DEL MICRO (TEMP, MENSAJE, MAC, ECT)
def find_string(pageString_s, start_s, end_s):
	htmlFind_s = "null";
	startFind = pageString_s.find(start_s)+len(start_s)
	endFind = pageString_s.find(end_s,startFind)
	htmlFind_s = pageString_s[startFind:endFind]
	return htmlFind_s

#FUNCION PARA LOG PYTHON
def init_logger():
	logger = logging.getLogger()
	logger.setLevel(logging.DEBUG)

	# create console handler and set level to info
	handler = logging.StreamHandler()
	handler.setLevel(logging.INFO)
	formatter = logging.Formatter("%(asctime)s-%(levelname)s - %(message)s", datefmt='%Y/%m/%d %H:%M:%S')
	handler.setFormatter(formatter)
	logger.addHandler(handler)

	#create error file handler and set level to error
#	handler = logging.FileHandler(filename="scriptError.log", encoding=None, delay="true")
	handler = logging.FileHandler("scriptError.log", 'a+')
	handler.setLevel(logging.ERROR)
	formatter = logging.Formatter("%(asctime)s-%(levelname)s - %(message)s", datefmt='%Y/%m/%d %H:%M:%S')
	handler.setFormatter(formatter)
	logger.addHandler(handler)

	# create debug file handler and set level to debug
	handler = logging.FileHandler(filename="scriptInfo.log", mode='a+')
	handler.setLevel(logging.DEBUG)
	formatter = logging.Formatter("%(asctime)s-%(levelname)s - %(message)s", datefmt='%Y/%m/%d %H:%M:%S')
	handler.setFormatter(formatter)
	logger.addHandler(handler)
