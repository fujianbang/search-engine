#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request

import json

from services.base import *
from services.api import ApiService
from settings import *

app = Flask(__name__)
app.debug = True

apiservice = ApiService()

@app.route("/")
def engine():
    return render_template('index.html', request_addr=REQUEST_ADDR)

@app.route("/search")
def search():
    """
    根据关键字查找信息
    default:10 limit
    """
    _keyword = request.args.get('wd')
    _page = request.args.get('page')
    if _page is None:
        _page = 1

    # 根据关键词从数据库中查找数据
    results = search_jobs_by_kw(_keyword, page=_page)
    return render_template('lists.html', keyword=_keyword, results=results['data'], total=results['total'], took=results['took'], current_page=_page, request_addr=REQUEST_ADDR)

@app.route("/api/language")
def api_language():
    return apiservice.language()

@app.route("/api/degree")
def api_degree():
    return apiservice.degree()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
