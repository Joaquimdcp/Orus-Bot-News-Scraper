from elasticsearch import Elasticsearch

es = Elasticsearch(
    ['ec2-54-191-86-108.us-west-2.compute.amazonaws.com'],
    port=9200
)

hola = {
    'prova': 'prova2'
}

res = es.index(index="test-index22222", doc_type='pis2', body=hola)
