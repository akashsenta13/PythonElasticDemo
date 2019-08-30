import requests
import json

headers = {'Content-type': 'application/json'}

def search(uri,term):
    query = json.dumps({
        "query" : {
            "match" : {
                "content" : term
            }
        }
    })
    response = requests.get(uri,data=query,headers=headers)
    results = json.loads(response.text)
    return results

def format_results(results):
    data = [doc for doc in results['hits']['hits']]
    for doc in data :
        print("%s) %s" % (doc["_id"],doc["_source"]["content"]))

def create_doc(uri,doc_data={}):
    query = json.dumps(doc_data)
    response = requests.post(uri,data=query,headers=headers)
    print(response)

if __name__ == "__main__":
    uri_search = "http://localhost:9200/test/articles/_search"
    uri_create = "http://localhost:9200/test/articles/"

    results = search(uri_search,"fox")
    format_results(results)

    #create_doc(uri_create,{"content":"The Fox!"})
    #results = search(uri_search,"Fox")
    #format_results(results)