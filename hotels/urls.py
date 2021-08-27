from django.urls import path

from . import views

app_name = 'hotels'
urlpatterns = [
	# path to enter the index of cities
	path('', views.index, name = 'index'),
	# path to select cities
	path('sel/', views.select_city, name = 'select'),
	# path showing the hotels in the selected city
	path('<str:city_name>/', views.results, name = 'result')
]