#!/usr/bin/env python
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import sys
import csv

argvs = sys.argv
argc = len(argvs)
if(argc < 2):
    print('Usage: # python %s zaim.csv' % argvs[0])
    quit()

actions = []
with open(argvs[1], 'r') as f:
    reader = csv.reader(f)
    header = next(reader)

    for i, row in enumerate(reader):
        action = {
            "_index": "zaim-%s" % row[0].split('-')[0],
            "_type": "zaim",
            "_id": int(i),
            "_source": {
                "@timestamp": row[0],
                "method": row[1],
                "category": row[2],
                "genre": row[3],
                "account": row[4],
                "receipt": row[5],
                "item": row[6],
                "memo": row[7],
                "place": row[8],
                "currency": row[9],
                "income": int(row[10]),
                "payment": int(row[11]),
                "transfer": int(row[12]),
                "balance": int(row[13]),
                "amount_before_translation": int(row[14]),
                "include": row[15]
            }
        }
        actions.append(action)

es = Elasticsearch("elasticsearch_elasticsearch_1:9200")

if len(actions) > 0:
    es.indices.delete(index='zaim*', ignore=[400, 404])
    helpers.bulk(es, actions)
