# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 18:15:28 2021

@author: Cub
"""
import sys
sys.path.append('C:\Cubs Files\Downloads')
from flask import Flask, render_template, request
import pandas as pd
import csv


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def index():
    
    return render_template('index.html')


@app.route('/data', methods=['GET', 'POST'])

def data():
    if request.method == 'POST':
        
        xfile = request.form['csvfile']
        
        data = []
        
        with open(xfile) as file:
            csvfile = csv.reader (xfile)
            for row in csvfile:
                data.append(row)
        
        return render_template('data.html', data=data)
if __name__ == '__main__':
    app.run(debug=True)