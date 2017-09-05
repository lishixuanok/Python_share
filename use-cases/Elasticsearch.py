from elasticsearch_dsl import Search
from elasticsearch import Elasticsearch

# elasticsearch_dsl documentation
# https://elasticsearch-dsl.readthedocs.io/en/latest/search_dsl.html
testClientList = ['your address']
testClient = Elasticsearch(testClientList)
shop_index = {"using": testClient, "index": "idx_shop", "doc_type": 'discount'}


def search(start=1, size=20):
    search = Search(**shop_index)
    print('Total is %s' % search.count())
    s = search[start:size]
    for hit in s.execute().hits.hits:
        # TODO: add your operation here
        print(hit)


if __name__ == '__main__':
    search()
