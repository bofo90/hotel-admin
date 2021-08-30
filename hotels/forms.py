from django import forms

from .models import City

class CityForm(forms.Form):
	"""
	A dropdown menu to show the available cities
	"""
	city_names = ((x.name, x.name) for x in City.objects.all())

	city_name = forms.ChoiceField(required = True, choices = city_names)
