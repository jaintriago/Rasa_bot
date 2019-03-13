import os
import urllib3
import requests
import json
from googletrans import Translator

translator = Translator()



def clima(ciudad):
	api_key = 'your apixu key' #your apixu key	
	try:
		mi_requests = 'http://api.apixu.com/v1/current.json?key=' + api_key + '&q=' + ciudad
		#quake_data = requests.get('http://api.apixu.com/v1/current.json?key=6ba7022b3599467494f61305191203&q=arequipa').json() 
		data = requests.get(mi_requests).json()
	except:
		print("nada")
		
	pais = data['current']['condition']['text'].lower()
		
	pais_es = translator.translate(pais, dest='es')

	print("Ciudad :" + str(data['location']['name']))
	print("País :" + str(data['location']['country']) + "\n")
	print("Temperatura :" + str(data['current']['temp_c']))
	print("Humedad :" + str(data['current']['humidity']))
	print("Condición :" + str(pais_es.text))
	print('\n')

clima("Cuzco")

