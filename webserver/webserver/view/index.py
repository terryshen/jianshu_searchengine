from django.shortcuts import render
from django.utils.safestring import mark_safe
from webserver.view.globaparasl import NumPerPage
from elasticsearch import Elasticsearch


def _(request):
    keywords = request.GET.get('keywords', '').strip()
    if keywords == '':
        return render(request, 'index.html', {
            'title': '简书站内搜索',
            'keywords': keywords,
            'err_info': '',
            'result': [],
        })
    else:
        result = get_elastic_search_result(keywords)
        if len(result) == 0:
            return render(request, 'index.html', {
                'title': '简书站内搜索',
                'keywords': keywords,
                'err_info': '无内容',
                'result': [],
            })
        else:
            error_infomat = '仅显示最多' + str(NumPerPage) + '条结果'
            return render(request, 'index.html', {
                'title': '简书站内搜索',
                'keywords': keywords,
                'err_info': error_infomat,
                'result': result,
            })


def get_highlight_title(item):
    try:
        title = mark_safe(' '.join(item['highlight']['articletitle'].text))
    except Exception as ex:
        title = item['_source']['articletitle']
        print('no highlight title ' + str(ex))
    finally:
        return title


def get_highlight_content(item):
    try:
        # 转化成text后会将原始文字全部输出，不转换会形成固定长度的文章内容
        # content = mark_safe(' '.join(item['highlight']['articlecontent'].text))
        content = mark_safe(' '.join(item['highlight']['articlecontent']))
    except Exception as ex:
        content = item['_source']['articlecontent']
        print('no highlight content ' + str(ex))
    finally:
        return content


def get_elastic_search_result(keywords):
    es = Elasticsearch([{'host': '127.0.0.1', 'port': 9200}])
    result = es.search(index='jianshu_full', doc_type='article_full', body={
        "query": {
            "bool": {
                "should": [
                    {
                        "match": {
                            "articletitle": keywords
                        }
                    },
                    {
                        "match": {
                            "articlecontent": keywords
                        }
                    }
                ]
            }
        },
        "highlight": {
            "fields": {
                "articletitle": {},
                "articlecontent": {}
            }
        },
        "from": 0,
        "size": NumPerPage
    })

    return [
        {
            'url': item['_source']['url'],
            'title': get_highlight_title(item),
            'content': get_highlight_content(item)
        }
        for item in result['hits']['hits']
    ]
