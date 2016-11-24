import logging
import os

def init_logger():
	logger = logging.getLogger()
	logger.setLevel(logging.DEBUG)
     
	# create console handler and set level to info
	handler = logging.StreamHandler()
	handler.setLevel(logging.INFO)
	formatter = logging.Formatter("%(asctime)s-%(levelname)s - %(message)s", datefmt='%Y/%m/%d %H:%M:%S')
	handler.setFormatter(formatter)
	logger.addHandler(handler)
 
	# create error file handler and set level to error
#	handler = logging.FileHandler(filename="scriptError.log", encoding=None, delay="true")
	handler = logging.FileHandler("scriptError.log", 'w+')
	handler.setLevel(logging.ERROR)
	formatter = logging.Formatter("%(asctime)s-%(levelname)s - %(message)s", datefmt='%Y/%m/%d %H:%M:%S')
	handler.setFormatter(formatter)
	logger.addHandler(handler)
 
	# create debug file handler and set level to debug
	handler = logging.FileHandler(filename="scriptInfo.log", mode='w+')
	handler.setLevel(logging.DEBUG)
	formatter = logging.Formatter("%(asctime)s-%(levelname)s - %(message)s", datefmt='%Y/%m/%d %H:%M:%S')
	handler.setFormatter(formatter)
	logger.addHandler(handler)
