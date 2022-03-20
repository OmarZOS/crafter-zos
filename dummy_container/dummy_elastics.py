
from elasticsearch import Elasticsearch
import json, requests

# create a client instance of Elasticsearch
elastic_client = Elasticsearch("http://localhost:9200")

# Python dictionary object representing an Elasticsearch JSON query:
search_param = {
    'query': {
        'match': {
            'field1': 'find me!'
        }
    }
}

for index in elastic_client.indices.get('*'):
      print (index)
# response = elastic_client.search(index="some_index", body=search_param)

# print (response)