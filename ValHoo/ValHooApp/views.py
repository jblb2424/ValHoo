from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models
from urllib.request import urlopen




def index(request):
    blank_plot = models.Plot("", [], 'line') #Initialize an empty plot
    print(sorted(blank_plot.index_dict.keys()))
    return render(request, 'home_page.html', {'plot': sorted(blank_plot.index_dict.keys())})

def new_plot(request):
   
    #Grabs the ticker and corresponding value to analyze
    ticker_name = request.POST.get('ticker', None) 
    multiple_values_name = request.POST.getlist('values')

    layout = request.POST.get('layout', 'line')

    #Initialize a new Plot
    new_plot = models.Plot(ticker_name, multiple_values_name, layout)
 
    ticker_data = new_plot.trace_data(new_plot.parse_data())

    #Offline html plot
    div_plot = new_plot.plot_offline_data(ticker_data)



    #Change url name when this is finished
    return render(request, 'home_page.html', {'url': div_plot, 'plot': sorted(new_plot.index_dict.keys())})

