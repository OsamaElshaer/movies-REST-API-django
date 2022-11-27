import elasticsearch
from elasticsearch_dsl import Search
from Blockter.settings import ELASTICSEARCH_DSL

ELASTIC_HOST = ELASTICSEARCH_DSL['default']['hosts']
client = elasticsearch.Elasticsearch(hosts=[ELASTIC_HOST])


def lookup(query, index='movie', fields=['title', 'overview']):
    if not query:
        return 
    results = Search(index=index).using(client).query("multi_match", fields=fields, fuzziness='AUTO', query=query)

    q_results = []

    for hit in results:
        data = {
            
            "title": hit.title,
            "overview": hit.overview,
            
        }
        q_results.append(data)
    return q_results
