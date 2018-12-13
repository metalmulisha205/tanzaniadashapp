# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 16:21:55 2018

@authors: Cole McKee, Viraj Khacker, Lonnie Webb, Aniket Pant
"""

import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

mapbox_access_token = "pk.eyJ1IjoibWV0YWxtdWxpc2hhMjA1IiwiYSI6ImNqa3p6MnMxZzB6aXMzd3FqNzIydGQ1eWQifQ.Q7-btpPLCXJol5KEae2fjA"
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Nuclear%20Waste%20Sites%20on%20American%20Campuses.csv')
dashLayout = html.Div(
    children=[
        '''Dash app coming soon!'''
    ],  
)