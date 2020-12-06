from elasticsearch import Elasticsearch
from jianshu_scrawler.database.es_connection import connect_elasticsearch, set_es_portnum, set_es_hostname


def store_records(elastic_object, index_name, doctype_name, record):
    is_stored = True
    try:
        outcome = elastic_object.index(index=index_name, doc_type=doctype_name, body=record)
        print(outcome)
    except Exception as ex:
        print('Error in indexing data')
        print(str(ex))
        is_stored = False
    finally:
        return is_stored


def create_index(es_object, index_name):
    created = False
    settings = {
        "mappings": {
            "article": {
                "properties": {
                    "id": {
                        "type": "text"
                    },
                    "url": {
                        "type": "text"
                    },
                    "metatitle": {
                        "type": "text",
                        "analyzer": "ik_max_word",
                        "search_analyzer": "ik_max_word"
                    },
                    "articletitle": {
                        "type": "text",
                        "analyzer": "ik_max_word",
                        "search_analyzer": "ik_max_word"
                    },
                    "metacontent": {
                        "type": "text",
                        "analyzer": "ik_max_word",
                        "search_analyzer": "ik_max_word"
                    },
                    "articlecontent": {
                        "type": "text",
                        "analyzer": "ik_max_word",
                        "search_analyzer": "ik_max_word"
                    },
                }
            }
        }
    }

    try:
        if not es_object.indices.exists(index_name):
            es_object.indices.create(index=index_name, ignore=400, body=settings)
            print('Created index')
        else:
            print('Exist index')
        created = True
    except Exception as ex:
        print(str(ex))
    finally:
        return created


def CreateIndices(indicesName):
    if len(indicesName) == 0:
        return
    host_name = '127.0.0.1'
    port_num = 9200
    set_es_hostname(host_name)
    set_es_portnum(port_num)
    es = connect_elasticsearch()
    if create_index(es, indicesName):
        print(indicesName + ' indexed successfully!')
    else:
        print(indicesName + ' indexd failed!')
    return
