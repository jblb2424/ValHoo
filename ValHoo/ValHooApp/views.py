from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models
from urllib.request import urlopen




def index(request):

    if request.method == 'POST':
        #Grabs the ticker and corresponding value to analyze
        ticker_name = request.POST.get('ticker', None) 
        # value_name = request.POST.get('value', None)

        multiple_values_name = request.POST.getlist('values')

        new_plot = models.Plot(ticker_name, multiple_values_name)
   
        ticker_data = new_plot.parse_data()

        #Offline html plot
        div_plot = new_plot.plot_offline_data(ticker_data)

        #Change url name when this is finished
        return render(request, 'home_page.html', {'url': div_plot})
    else:
        return render(request, 'home_page.html')