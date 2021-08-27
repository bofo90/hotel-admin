import requests, csv

from django.test import TestCase

from hotels.models import City, Hotel
from django.conf import settings

from hotels.modcreator import *

class ModelCreatorTest(TestCase):

	def test_conection(self):
		""" Test if the connection is correct """
		city_r = requests.get(settings.CITY_CSV, auth=(settings.CSV_USERNAME, settings.CSV_PASSWORD))
		hotel_r = requests.get(settings.HOTEL_CSV, auth=(settings.CSV_USERNAME, settings.CSV_PASSWORD))

		self.assertEqual(city_r.status_code, 200)
		self.assertEqual(hotel_r.status_code, 200)

	def test_city_data(self):
		""" Test if the data of the city has the proper shape """
		list_city = download_from_api(settings.CITY_CSV)

		for elem in list_city:
			self.assertEqual(len(elem),2)

	def test_hotel_data(self):
		""" Test is the data of the hotels has the proper shape """
		list_hotel = download_from_api(settings.HOTEL_CSV)

		for elem in list_hotel:
			self.assertEqual(len(elem),3)

