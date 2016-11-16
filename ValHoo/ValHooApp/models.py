from __future__ import unicode_literals
from django.db import models
import plotly
import plotly.plotly as py
from plotly.graph_objs import *
from xml.dom import minidom
import urllib
import json
from pprint import pprint



# p = py.sign_in("jblb2424", "Peg24lee")
# plotly('jblb2424', 'yi6kip4q4i')  # this is YOUR account information from plotly


plotly.tools.set_credentials_file(username='jblb2424', api_key='yi6kip4q4i')




def parse_data(ticker, data):
	url_str = 'http://edgaronline.api.mashery.com/v2/corefinancials/ann?primarysymbols='+ticker+'&appkey=qmhuw98c4cacxsr5j559gbwn'

	#For some reason the API is shown as XML in browser
	#But is interpreted as JSON when grabbed form URL
	#Treat it as JSON!

	#To reach any value...j_obj['result']['rows'][*YEAR(0-3)*]['values'][*ITEM INDEX*]['value']

	online_json = urllib.urlopen(url_str)
	j_obj = json.load(online_json)
	# print(j_obj['result']['rows'][0]['values'][46]['value'])

	#revenue
	yr_one = j_obj['result']['rows'][0]['values'][46]['value']
	yr_two = j_obj['result']['rows'][1]['values'][46]['value']
	yr_three = j_obj['result']['rows'][2]['values'][46]['value']
	yr_four = j_obj['result']['rows'][3]['values'][46]['value']

	trace0 = Scatter(
	    x=[1, 2, 3, 4],
	    y=[yr_one, yr_two, yr_three, yr_four]
	)

	data = Data([trace0])
	return data

def plot_data(data):
	# layout = {
	# title: 'Here is Your Graph',
	# showlegend: false}
	# plot_url = py.plot(parse_data('msft, 'revenue'), filename = 'basic-line', sharing = 'public', auto_open = False)
	plot_url = py.plot(data, filename = 'basic-line', sharing = 'public', auto_open = False)
	return plot_url
