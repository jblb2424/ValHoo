from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def index(request):
	# return HttpResponse('''<iframe width="800" height="600" frameborder="0" seamless="seamless" scrolling="no" src="https://plot.ly/~jblb2424/0/.embed?width=800&height=600"></iframe>''')
	return render(request, 'home_page.html')

def get_ticker(request):
	print(request.POST.get('ticker', None))

