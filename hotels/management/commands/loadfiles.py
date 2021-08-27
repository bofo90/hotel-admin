from django.core.management.base import BaseCommand

from hotels.modcreator import *

class Command(BaseCommand):

	"""
	Custom command to be run with python manage.py loadfiles in order to 
	retrieve data from the API through http request.
	"""

	def handle(self, *args, **kwargs):

		create_city_models()
		create_hotel_models()