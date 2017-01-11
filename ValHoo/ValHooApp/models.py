from __future__ import unicode_literals
from django.db import models
import plotly
import plotly.plotly as py
from plotly.graph_objs import *
import urllib
import json
import plotly.graph_objs as go
from urllib.request import urlopen


# p = py.sign_in("jblb2424", "Peg24lee")
# plotly('jblb2424', 'yi6kip4q4i')  # this is YOUR account information from plotly


plotly.tools.set_credentials_file(username='jblb2424', api_key='yi6kip4q4i')

class Plot():

	def __init__(self, ticker, data):
		self.ticker = ticker
		self.data = data


	index_dict = {
		'Change in Current Assets': 26, 
		'Change in Current Liabilities': 27, 
		'Change in Inventories': 28, 
		'Dividends Paid': 29, 
		'Effect of Exchange Rate on Cash': 30, 
		'Capital Expenditures': 31, 
		'Cash from Financing Activities': 32, 
		'Cash From Investing Activities': 33,
		'Cash From Operating Activities': 34,
		'CF Depreciation Amorization': 35,
		'Change in Accounts Receivable': 36,
		'Net Investment Changes': 37,
		'Net Change in Cash': 38,
		'Total Adjustments': 39,
		'Earnings Before Interest and Taxes': 40,
		'Cost of Revenue': 41,
		'Equity Earnings': 42,
		'Gross Profit': 43,
		'Income Before Taxes': 44,
		'Interest Expense': 45,
		'Net Income': 46,
		'Net Income Applicable to Common': 47,
		'Revenue': 48,
		'Selling General Administrative Expenses': 49,
		'Common Stock':50,
		'Cash and Cash Equivalents': 51,
		'Cash Equivalents and Short Term Investments': 52,
		'Inventories Net': 53,
		'Minority Interest': 54,
		'Other Assets': 55,
		'Other Liabilities': 56,
		'Property Plant Eqipment Net': 57,
		'Retained Earnings': 58,
		'Total Assets': 59,
		'Total Current Assets': 60,
		'Total Current Liabilities': 61,
		'Total Liabilities': 62,
		"Total Long Term Debt": 63,
		"Total Receivables Net": 64,
		"Total Stockholders Equity": 65,
		"Treasury Stock": 66
		}

	def parse_data(self):
		url_str = 'http://edgaronline.api.mashery.com/v2/corefinancials/ann?primarysymbols='+self.ticker+'&appkey=edj5xvdz9gz23mds4tpu8bdd'
		list_of_graphs = []


		#For some reason the API is shown as XML in browser
		#But is interpreted as JSON when grabbed form URL
		#Treat it as JSON!

		#To reach any value...j_obj['result']['rows'][*YEAR(0-3)*]['values'][*ITEM INDEX*]['value']
		online_json = urllib.request.urlopen(url_str)
		str_response = online_json.read().decode('utf-8')
		j_obj = json.loads(str_response)


		company_name = j_obj['result']['rows'][0]['values'][1]['value']


		#Compartamentalizes data into x(year) and y(values) for each selection the user makes
		for selection in self.data:

			index_of_selection = self.index_dict[selection]

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

		retrieved_data = Data(list_of_graphs)
		compiled_company_information = {"data": retrieved_data, "name": company_name}
		return compiled_company_information



	def plot_offline_data(self, company_info):
		print(company_info['data'])
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