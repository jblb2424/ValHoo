from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import TickerForm
import models


# def index(request):
# 	# return HttpResponse('''<iframe width="800" height="600" frameborder="0" seamless="seamless" scrolling="no" src="https://plot.ly/~jblb2424/0/.embed?width=800&height=600"></iframe>''')
# 	return render(request, 'home_page.html')



def get_ticker(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        ticker_name = request.POST.get('ticker', None)
        ticker_data = models.parse_data(ticker_name, 'revenue')
        #Online plot
        # url = models.plot_data(ticker_data)
        #Offline html plot
        div_plot = models.plot_offline_data(ticker_data)
   
        #Change url names when this is finished
        return render(request, 'home_page.html', {'url': div_plot})
    else:
        return render(request, 'home_page.html')