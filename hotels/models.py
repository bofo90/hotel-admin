from django.db import models

class City(models.Model):
	"""
	Stores the cities where the hotels are with a simplified code.
	"""
	name = models.CharField(max_length = 200)
	code = models.CharField(max_length = 50)

	def __str__(self):
		return self.name

class Hotel(models.Model):
	"""
	Stores the hotel pointing to a city with name and code.
	"""
	city = models.ForeignKey(City, on_delete = models.CASCADE)
	name = models.CharField(max_length = 200)
	code = models.CharField(max_length = 50)

	def __str__(self):
		return self.name