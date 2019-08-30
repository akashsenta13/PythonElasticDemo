from elasticsearch import Elasticsearch

if __name__ == "__main__":
    es = Elasticsearch()
    res = es.search(index="test",body={"query":{"match":{"content":"fox"}}})
    print("%d documents found:" % res['hits']['total']['value'])
    for doc in res['hits']['hits']:
        print("%s) %s" % (doc["_id"],doc["_source"]["content"]))


    #es.create(index="test",doc_type="articles",id=5,body={"content":"one more fox"})