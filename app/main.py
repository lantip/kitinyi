#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
__version__     =   "0.0.1"
__author__      =   "@lantip"
__date__        =   "2020/11/03"
__description__ =   "Kitinyi Giniritir"
"""

import os, json
from flask import Flask, request, jsonify, render_template
from kiti import bikin


app = Flask(__name__, template_folder="example", static_folder="example")
app.config.from_pyfile('settings.cfg')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/', methods=['GET'])
def index():
    text = request.args.get('q')
    if text:
    	result  = bikin(text)
    else:
    	result = {
    		'status': 'ERROR',
    		'message': 'Gunakan ?q di url. contoh: http://url-nya/?q=hanya kekeliruan teknis administratif'
    	}

    return jsonify(result)
