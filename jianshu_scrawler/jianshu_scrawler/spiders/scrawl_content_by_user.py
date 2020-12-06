import os
import codecs
import random

from bs4 import BeautifulSoup
import requests
import time
import datetime
from jianshu_scrawler.path.path_file import get_files_path, get_files_path_userid
from jianshu_scrawler.path.config_setting import user_agent


def extract_user_id_set(html_content):
    result = set()
    soup = BeautifulSoup(html_content, 'lxml')
    list_container = soup.find('div', id='list-container')
    if not list_container:
        return result
    user_num = 0
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    for link in list_container.find_all('a', class_='title'):
        result.add(link.get('href').replace('/p/', ''))
    return result


def get_article_id_set(user):
    page = 1
    headers = {'User-Agent': random.choice(user_agent)}
    id_set = set()

    while True:
        url = 'http://www.jianshu.com/u/{0}?order_by=shared_at&page={1}'.format(user, page)
        print(url)
        resp = requests.get(url, headers=headers)
        result = extract_user_id_set(resp.text)
        if result.issubset(id_set):
            break
        else:
            id_set = id_set.union(result)
        print('-----------')
        page += 1
        # time.sleep(1)
    return id_set


def download_articles(id_set, user_id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, Llike Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    # dir_path = get_files_path()
    dir_path = get_files_path_userid(user_id)

    for article_id in id_set:
        url = 'http://www.jianshu.com/p/{0}'.format(article_id)
        print('download {0}'.format(url))
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            file_path = os.path.join(dir_path, '{0}.html'.format(article_id))
            with codecs.open(file_path, 'w', encoding='utf-8') as f:
                print('save: ' + '{0}.html'.format(article_id))
                f.write(resp.text)


def download_articles_userid(user_id):
    id_set = get_article_id_set(user_id)
    download_articles(id_set, user_id)