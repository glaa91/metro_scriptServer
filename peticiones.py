#!usr/bin/python3
import lxml 
import html
import urllib.request, urllib.error

print("*******************************************************************************************************************")
print("ver. 20161117")
print()
print()

url_s = "http://172.21.8.17/runtime.shtml"
try:
	f = urllib.request.urlopen(url_s)
#responseCode_i = f.getcode()
#print("RESPONSE CODE: " + str(responseCode_i))
	
except urllib.error.HTTPError as e:
	# Return code error (ex 404, 501, ...)
	print('HTTP ERROR... CODE:' + str(f.getcode()))

except urllib.error.URLError as e:
	# not an HTTP-specific error (ex. conection refused)
	print('URL ERROR...')

else:
	#200
	print('GOOD... CODE: ' + str(f.getcode()))

	pageString_s = str(f.read())

	startTemp_s = "Temperatura = "
	startFuente5v_s = "Fuente 5 volt = "
	startFuente24v_s = "Fuente 24 Volt Semaforos = "
	startFuentePpic_s = "Estado PPIC = "
	startFuente5pic_s = "Fuente Display 5 volt = "
	startMensaje_s = "Mensaje = "
	endTemp_s = "&#"
	end_s = " \\r\\n"
	endMensaje_s = "$</pre>" 

	#CONTENIDO
	print()
	print("CONTENT: " + pageString_s)
	print()
	print()

	#TEMPERATURA
	startTemp = pageString_s.find(startTemp_s)+len(startTemp_s)
	endTemp = pageString_s.find(endTemp_s,startTemp)
	print("TEMP:" + pageString_s[startTemp:endTemp])

	#FUENTE 5v
	startFuente5v = pageString_s.find(startFuente5v_s)+len(startFuente5v_s)
	endFuente5v = pageString_s.find(end_s,startFuente5v)
	print("FUENTE 5v:" + pageString_s[startFuente5v:endFuente5v])

	#FUENTE 24v
	startFuente24v = pageString_s.find(startFuente24v_s)+len(startFuente24v_s)
	endFuente24v = pageString_s.find(end_s,startFuente24v)
	print("FUENTE 24v:" + pageString_s[startFuente24v:endFuente24v])

	#FUENTE PPIC
	startFuentePpic = pageString_s.find(startFuentePpic_s)+len(startFuentePpic_s)
	endFuentePpic = pageString_s.find(end_s,startFuentePpic)
	print("FUENTE PPIC:" + pageString_s[startFuentePpic:endFuentePpic])

	#FUENTE 5PIC
	startFuente5pic = pageString_s.find(startFuente5pic_s)+len(startFuente5pic_s)
	endFuente5pic = pageString_s.find(end_s,startFuente5pic)
	print("FUENTE 5PIC:" + pageString_s[startFuente5pic:endFuente5pic])

	#MENSAJE
	startMensaje = pageString_s.find(startMensaje_s)+len(startMensaje_s)
	endMensaje = pageString_s.find(endMensaje_s,startMensaje)
	print("MENSAJE:" + pageString_s[startMensaje:endMensaje])
