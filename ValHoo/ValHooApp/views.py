from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import TickerForm
import models


# def index(request):
# 	# return HttpResponse('''<iframe width="800" height="600" frameborder="0" seamless="seamless" scrolling="no" src="https://plot.ly/~jblb2424/0/.embed?width=800&height=600"></iframe>''')
# 	return render(request, 'home_page.html')



def get_ticker(request):
  
    if request.method == 'POST':
        #Grabs the ticker and corresponding value to analyze
        ticker_name = request.POST.get('ticker', None) 
        # value_name = request.POST.get('value', None)
        print(ticker_name)
        multiple_values_name = request.POST.getlist('values')
   
        ticker_data = models.parse_data(ticker_name, multiple_values_name)

        #Online plot
        # url = models.plot_data(ticker_data)
        #Offline html plot
        div_plot = models.plot_offline_data(ticker_data)

        #Change url name when this is finished
        return render(request, 'home_page.html', {'url': div_plot})
    else:
        return render(request, 'home_page.html')