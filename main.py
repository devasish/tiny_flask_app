#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 08:00:00 2020

@author: deva
"""
print(__file__)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello from docker...using bind mount"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4040, debug=True)
