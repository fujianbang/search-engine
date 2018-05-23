#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch

import logging

logger = logging.getLogger(__name__)

es = Elasticsearch()
ES_INDEX_JOBS = "jobs-index"

def search_jobs_by_kw(kw, page, size=10):
    _query_statement={
        'query': {
            'match': {
                'job_name': kw
            }
        }
    } 
    length = es.search(index=ES_INDEX_JOBS, body=_query_statement)['hits']['total']
    results = es.search(index=ES_INDEX_JOBS, body=_query_statement, from_=page, size=size)
    data = []
    for hit in results['hits']['hits']:
        data.append(hit['_source'])

    return data, results['hits']['total']

