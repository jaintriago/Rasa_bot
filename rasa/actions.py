from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import os
import urllib3
import requests
import json
from googletrans import Translator

translator = Translator()

class ActionWeather(Action):
	def name(self):
		return 'action_weather'
		
	def run(self, dispatcher, tracker, domain):
		from apixu.client import ApixuClient
		api_key = 'your apixu key' #your apixu key
		#client = ApixuClient(api_key)
		
		loc = tracker.get_slot('ubicacion')
		#current = client.getCurrentWeather(q=loc)
		try:
			mi_requests = 'http://api.apixu.com/v1/current.json?key=' + api_key + '&q=' + loc
			data = requests.get(mi_requests).json()
		except:
			print("Error al conectar")
			
		pais = data['current']['condition']['text'].lower()
		pais_es = translator.translate(pais, dest='es')
		
		country = data['location']['country']
		city = data['location']['name']
		condition = pais_es.text
		temperature_c = data['current']['temp_c']
		humidity = data['current']['humidity']
		wind_mph = data['current']['wind_mph']

		response = """Está {} en {} actualmente. La temperatura es {} grados, La humedad es {} % y la velocidad del viento es {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
						
		dispatcher.utter_message(response)
		return [SlotSet('ubicacion',loc)]

