# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 18:15:28 2021

@author: Cub
"""
import codecs
import csv
import sys
from io import StringIO
import pandas as pd
from numpy import genfromtxt
import base64
from io import BytesIO


sys.path.append('C:\Cubs Files\Downloads')
import os
from flask import Flask, flash, request, redirect, url_for, render_template, send_file, jsonify
from werkzeug.utils import secure_filename

import matplotlib.pyplot as plt


UPLOAD_FOLDER = './static'
STATIC = './static'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('file',
                                    filename=filename))
    return render_template('index.html')


# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)


@app.route('/<filename>')
def file(filename):
    filex = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    data = pd.read_csv(filex)
    print(data.head())
    plt.plot(data["Total Sale"])
    plt.plot(data["Instore Sale"])
    plt.plot(data["Cafe Sale"])

    # return render_template('plot.html', name=plt.show())

    img = BytesIO()
    plt.savefig(img, format='png')
   # plt.close()
    img.seek(0)

    #plot = plt.savefig(os.path.join(app.config['STATIC'], "lot"))
    plot = plt.savefig(os.path.join(app.config['UPLOAD_FOLDER'],  'logo'))

    return render_template('plot.html')

   # return send_file(os.path.join(app.config['UPLOAD_FOLDER'], "lot.png"), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
