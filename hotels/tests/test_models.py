from django.test import TestCase

from hotels.models import City, Hotel

def create_city(name, code):

	return City.objects.create(name = name, code = code)

def create_hotel(city, name, code):

	return Hotel.objects.create(city = city, name = name, code = code)

class CityTests(TestCase):

	def test_creation_city(self):
		""" Test if the creation of a city is correct """
		city = create_city('Mexico City', 'MEX')
		self.assertTrue(isinstance(city,City))
		self.assertEqual(city.name, 'Mexico City')
		self.assertEqual(city.code, 'MEX')

	"""
	Further tests:
	the code is unique
	the code has only 3 letters
	the code follows international standards
	new cities are unique
	no weird characters in the city name
	""" 


class HotelTests(TestCase):

	def test_creation_hotel(self):
		""" Test if the creation of a hotel is correct """
		city = create_city('Mexico City', 'MEX')
		hotel = create_hotel(city,'Hilton Centro Historico', 'MEX99')
		self.assertTrue(isinstance(hotel,Hotel))
		self.assertTrue(isinstance(hotel.city,City))
		self.assertEqual(hotel.city.name, 'Mexico City')
		self.assertEqual(hotel.city.code, 'MEX')
		self.assertEqual(hotel.name, 'Hilton Centro Historico')
		self.assertEqual(hotel.code, 'MEX99')

	"""
	Further tests:
	new hotels are unique in the city
	the city of a hotel exist
	the code of the hotel is unique
	the code has 5 letters
	the code corresponds to a city + 2 more numbers
	no weird characters in the hotel name
	"""