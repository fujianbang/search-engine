#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch

import logging

logger = logging.getLogger(__name__)

es = Elasticsearch()
ES_INDEX_JOBS = "jobs-index"

def search_jobs_by_kw(kw, page, size=10):

    if "c:" in kw or "d:" in kw or "r:" in kw:
        # 复杂搜索(公司|学历|地区)
        # c:新浪 d:学历 r:成都 java
        _query_statement={
            'query': {
                'bool': {
                    'must':[
                    ]
                }
            }
        }
        for item in kw.split(" "):
            if "c:" in item:
                _company_name = item.split(":")[1]
                _query_statement['query']['bool']['must'].append({'match':{'company_name':_company_name}})
            elif "d:" in item:
                _degree = item.split(":")[1]
                _query_statement['query']['bool']['must'].append({'match':{'job_require_degree':_degree}})
            elif "r:" in item:
                _regin = item.split(":")[1]
                _query_statement['query']['bool']['must'].append({'match':{'regin':_regin}})
            else:
                _query_statement['query']['bool']['must'].append({'match':{'job_name':item}})

    else:
        # 简单接口
        _query_statement={
            'query': {
                'match': {
                    'job_name': kw
                }
            }
        } 
    # 结果数量
    length = es.search(index=ES_INDEX_JOBS, body=_query_statement)['hits']['total']
    # 搜索结果（一次一页十条）
    results = es.search(index=ES_INDEX_JOBS, body=_query_statement, from_=page, size=size)

    data = []
    for hit in results['hits']['hits']:
        data.append(hit['_source'])

    return {'data':data, 'total':results['hits']['total'], 'took':results['took']}

