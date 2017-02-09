from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models
from urllib.request import urlopen
from plotly.offline import download_plotlyjs, plot




def index(request):
    blank_plot = models.Plot("", [], 'line') #Initialize an empty plot
    print(sorted(blank_plot.index_dict.keys()))
    return render(request, 'home_page.html', {'plot': sorted(blank_plot.index_dict.keys())})

def new_plot(request):
   
    #Grabs the ticker and corresponding value to analyze
    ticker_name = request.POST.get('ticker') 
    #Error handling if there is no ticker name inputted
    if not ticker_name:
        print("ERROR, NO STOCK TICKER ENTERED")
        ticker_name = 'AAPL'

 
    multiple_values_name = request.POST.getlist('values')
    print (multiple_values_name)
    #Error handling if no analysis selection is inputted
    if not multiple_values_name:
        print("ERROR, NO ANALYSIS SELECTION CHECKED")
        multiple_values_name = ['Revenue']
    #ticker_name = request.POST.get('ticker', None) 
    

    layout = request.POST.get('layout', 'line')

    #Initialize a new Plot
    new_plot = models.Plot(ticker_name, multiple_values_name, layout)

    ticker_data = new_plot.trace_data(new_plot.parse_data())

    #Offline html plot
    div_plot = new_plot.plot_offline_data(ticker_data)



    #Stock Value of Plot Ticker
    stock_value = new_plot.get_stock_value()

    #Change url name when this is finished
    return render(request, 'home_page.html', {'url': div_plot, 'plot': sorted(new_plot.index_dict.keys()), 'stock': stock_value})
    
    #return render(request, 'home_page.html', {'plot': sorted(blank_plot.index_dict.keys())})
 

