
from flask import Flask
from flask import render_template
#import any libraries needed - prolly won't need these in this app.py file tho 
#instead they might be used in dashLayout.py
import pandas as pd
import numpy as np

#Imports for dash-related stuff
import dash 
import os

import dashLayout #this is referring to another python file where the dash layout is created
#############################

Server = Flask(__name__)
App = dash.Dash(__name__, server=Server, url_base_pathname='/dashapp/')

# Load styles
css_bootstrap_url = ''
App.css.append_css({
    "external_url": [css_bootstrap_url],
})


################################
#####START Graph PAGE LAYOUT####
###############################
App.layout = dashLayout.dashLayout
################################
#####END Graph PAGE LAYOUT####
###############################
@Server.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    Server.run(debug=True)
