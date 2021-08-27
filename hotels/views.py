from django.shortcuts import get_object_or_404, render, reverse
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader

from .models import City, Hotel

class IndexView(generic.ListView):
	"""
	Use of generic view to list all cities that are on the database and 
	display it according to hotels/index.html
	"""
	template_name = 'hotels/index.html'
	context_object_name = 'all_cities'

	def get_queryset(self):
		""" Return all the cities for display """
		return City.objects.order_by('name')

def select_city(request):
    
    try:
        selected_choice = City.objects.get(pk=request.POST['city'])
        print(selected_choice)
    except (KeyError, City.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'hotels/index.html', {
            'error_message': "You didn't select a choice.",
            'all_cities' : City.objects.order_by('name')
        })
    else:
        # selected_choice.votes += 1
        # selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('hotels:result', args=(selected_choice.name,)))


def results(request, city_name):
	"""
	Create view that displays the hotels in a city following hotels/results.html
	"""
	c = get_object_or_404(City, name = city_name)
	hotels_in_city = Hotel.objects.filter(city__name = city_name)
	context = {
		'hotels_in_city' : hotels_in_city,
		'city_name' : city_name,
	}

	return render(request, 'hotels/result.html', context)
