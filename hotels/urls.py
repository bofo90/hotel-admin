from django.urls import path

from . import views

app_name = 'hotels'
urlpatterns = [
	# path to enter the index of cities
	path('', views.IndexView.as_view(), name = 'index'),
	# path showing the hotels in the selected city
	path('<str:city_name>/', views.results, name = 'result')
]