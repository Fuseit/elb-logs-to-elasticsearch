import requests
import os

# Get ES url from environment variables
es_url = os.getenv("ELASTICSEARCH_URL", False)

if not es_url:
    print('************ ERROR: No elasticsearch URL defined *************')
    exit()

def put_document(index, mapping, doc):
    try:
        url = es_url + '/' + index + '/' + mapping + '/'
        req = requests.post(url, doc)
        return req.text
    except Exception as e:
        print(e)
        exit()
