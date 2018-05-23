#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request

from es_search import *

app = Flask(__name__)
app.debug = True

@app.route("/")
def engine():
    return render_template('index.html')

@app.route("/search")
def search():
    """
    根据关键字查找信息
    default:10 limit
    """
    keyword = request.args.get('wd')
    page = request.args.get('page')
    if page is None:
        page = 1

    # 根据关键词从数据库中查找数据
    data, length = search_jobs_by_kw(keyword, page=page)
    return render_template('lists.html', keyword=keyword, results=data, length=length, current_page=page)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
