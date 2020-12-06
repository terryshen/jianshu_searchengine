from elasticsearch import Elasticsearch

host_name = '127.0.0.1'
port_num = 9200
index_name = 'jianshu_full'
doctype_name = 'article_full'


def set_es_hostname(hostname):
    host_name = hostname
    return


def set_es_portnum(portnum):
    port_num = portnum


def set_es_indexname(indexname):
    index_name = indexname
    return


def set_es_doctypename(doctypename):
    doctype_name = doctypename
    return;


def get_es_indexname():
    return index_name


def get_es_doctypename():
    return doctype_name


def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': host_name, 'port': port_num}])
    if _es.ping():
        print('Yay Connected')
    else:
        print('Awww it coult not connected!')
    return _es
