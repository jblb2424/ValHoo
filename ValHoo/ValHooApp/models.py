from __future__ import unicode_literals
from django.db import models
import plotly
import plotly.plotly as py
from plotly.graph_objs import *
import urllib
import json
import plotly.graph_objs as go




# p = py.sign_in("jblb2424", "Peg24lee")
# plotly('jblb2424', 'yi6kip4q4i')  # this is YOUR account information from plotly


plotly.tools.set_credentials_file(username='jblb2424', api_key='yi6kip4q4i')

def parse_data(ticker, data_to_grab):
	url_str = 'http://edgaronline.api.mashery.com/v2/corefinancials/ann?primarysymbols='+ticker+'&appkey=qmhuw98c4cacxsr5j559gbwn'
	list_of_graphs = []

	index_dict = {
	'change in current assets': 25, 
	'change in current liabilities': 26, 
	'change in inventories': 27, 
	'dividends paid': 28, 
	'effect of exchange rate on cash': 29, 
	'capital expenditures': 30, 
	'cash from financing activities': 31, 
	'cash from investing activities': 32,
	'cash from operating activities': 33,
	'revenue': 46
	
	}

	#For some reason the API is shown as XML in browser
	#But is interpreted as JSON when grabbed form URL
	#Treat it as JSON!

	#To reach any value...j_obj['result']['rows'][*YEAR(0-3)*]['values'][*ITEM INDEX*]['value']
	online_json = urllib.urlopen(url_str)
	j_obj = json.load(online_json)


	company_name = j_obj['result']['rows'][0]['values'][1]['value']

	#Compartamentalizes data into x(year) and y(values) for each selection the user makes
	for selection in data_to_grab:

		index_of_selection = index_dict[selection]

		#Data for each year that corresponds to index of selection
		yr_one = j_obj['result']['rows'][0]['values'][index_of_selection]['value']
		yr_two = j_obj['result']['rows'][1]['values'][index_of_selection]['value']
		yr_three = j_obj['result']['rows'][2]['values'][index_of_selection]['value']
		yr_four = j_obj['result']['rows'][3]['values'][index_of_selection]['value']

		trace = go.Scatter(
		    x=[1, 2, 3, 4],
		    y=[yr_one, yr_two, yr_three, yr_four],
		    name=selection
		)

		list_of_graphs.append(trace)

	data = Data(list_of_graphs)
	compiled_company_information = {"data": data, "name": company_name}
	return compiled_company_information
#Online Plot...not used as of right now
def plot_data(data):
	# plot_url = py.plot(parse_data('msft, 'revenue'), filename = 'basic-line', sharing = 'public', auto_open = False)
	plot_url = py.plot(data, filename = 'basic-line', sharing = 'public', auto_open = False)
	return plot_url

def plot_offline_data(company_info):
	layout = go.Layout(
    title=company_info["name"],
    xaxis=dict(
        title='Year',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Value',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
	)
	fig = go.Figure(data=company_info['data'], layout=layout)
	offline = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
	return offline