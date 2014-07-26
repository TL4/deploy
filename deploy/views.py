# coding: utf-8
from subprocess import check_output
from flask import render_template as tpl
from . import app


@app.route('/')
def index():
    return tpl("index.html")


@app.route('/run')
def run_cmd():
    output = check_output('ls -l', shell=True)
    ctx = {'output': output.split('\n')}
    return tpl("index.html", **ctx)