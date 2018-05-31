#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

from elasticsearch import Elasticsearch

import json

class ApiService(object):

    def __init__(self):
        self.ES_INDEX = "jobs-index"
        self.es = Elasticsearch()

    def get_from_es(self, _query_statment):
        return self.es.search(index=self.ES_INDEX, body=_query_statment)['hits']['total']

    def language(self):
        def _query_statment(kw):
            return {'query':{'match':{'job_name':kw}}}
        
        java_count = self.get_from_es(_query_statment('java'))
        c_count = self.get_from_es(_query_statment('c++'))
        python_count = self.get_from_es(_query_statment('python'))
        js_count = self.get_from_es(_query_statment('js'))
        php_count = self.get_from_es(_query_statment('php'))
        
        _ios_count = self.get_from_es(_query_statment('ios'))
        swift_count = self.get_from_es(_query_statment('swift')) + _ios_count

        go_count = self.get_from_es(_query_statment('c++'))

        return json.dumps({'java':java_count, 'c':c_count, 'python':python_count, 'js':js_count, 'php':php_count, 'swift':swift_count, 'go':go_count})

    def degree(self):
        def _query_statment(kw):
            return {'query':{'match':{'job_require_degree':kw}}}

        d0 = self.get_from_es(_query_statment('高')) # 初高中
        d1 = self.get_from_es(_query_statment('中专'))
        d2 = self.get_from_es(_query_statment('大专'))
        d3 = self.get_from_es(_query_statment('本科'))
        d4 = self.get_from_es(_query_statment('硕士'))
        d5 = self.get_from_es(_query_statment('博士'))

        return json.dumps({'d0':d0, 'd1':d1, 'd2':d3, 'd3':d3, 'd4':d4, 'd5':d5})
