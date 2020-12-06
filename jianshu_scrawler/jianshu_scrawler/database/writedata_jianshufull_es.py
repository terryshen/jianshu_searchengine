import os
import codecs
from jianshu_scrawler.path.path_file import get_files_path_userid
from jianshu_scrawler.database.es_connection import connect_elasticsearch, get_es_indexname, get_es_doctypename
from bs4 import BeautifulSoup


def process_text(text):
    '''将换行，多个空格替换成一个空格'''
    text = text.strip().replace('\n', ' ')
    return ' '.join(text.split())


def WriteData_In_Elastic(userid):
    file_dir = get_files_path_userid(userid)
    for filename in os.listdir(file_dir):
        if filename.endswith('html'):
            print(filename)
            file_path = os.path.join(file_dir, filename)
            article_id = filename.replace('.html', '')
            url = 'http://www.jianshu.com/p/{0}'.format(article_id)
            html_content = codecs.open(file_path, 'r', encoding='utf-8')
            soup = BeautifulSoup(html_content, 'lxml')
            try:
                thing = soup.find('title')
                if thing:
                    metatitle = soup.find('title').text
                else:
                    continue
            except Exception as ex:
                continue
            try:
                thing = soup.find('h1', class_='_2zeTMs')
                if thing:
                    articletitle = soup.find('h1', class_='_2zeTMs').text
                else:
                    continue
            except Exception as ex:
                continue
            try:
                thing = soup.find(attrs={"name": "description"})['content']
                if thing:
                    metacontent = soup.find(attrs={"name": "description"})['content']
                else:
                    continue
            except Exception as ex:
                continue
            try:
                thing = soup.find('article', class_='_2rhmJa')
                if thing:
                    articlecontent = soup.find('article', class_='_2rhmJa').text
                else:
                    continue
            except Exception as ex:
                continue

            es = connect_elasticsearch()
            result = {
                'id': article_id, 'url': url,
                'metatitle': process_text(metatitle), 'articletitle': process_text(articletitle),
                'metacontent': process_text(metacontent), 'articlecontent': process_text(articlecontent)
            }
            es.index(index=get_es_indexname(), doc_type=get_es_doctypename(), body=result)
