import os
import requests
import time
from bs4 import BeautifulSoup
import codecs
import random
from jianshu_scrawler.path.config_setting import user_agent
from jianshu_scrawler.path.path_file import get_user_path


#def get_user_path():
#    # dir_path = os.path.join(os.path.dirname(os.getcwd()), 'users')
#    dir_path = os.path.dirname(os.path.realpath(__file__))
#    dir_path = os.path.dirname(dir_path)
#    dir_path = os.path.join(dir_path, 'user')
#    if not os.path.exists(dir_path):
#        os.makedirs(dir_path)
#    return dir_path


def extract_user_id_set(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    result = set()
    user_num = 0
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    for link in soup.find_all('a', target='_blank'):
        user = link.get('href')
        if user.find('/users') != -1:
            user = link.get('href').replace('/users/', '')
            result.add(user)
            file_path = os.path.join(get_user_path(), 'user.txt')
            with codecs.open(file_path, 'a', encoding='utf-8') as f:
                f.write(user)
                f.write('\n')
                user_num += 1
        else:
            continue
    print(str(user_num) + ' users have been saved!')
    return result


def get_article_id_sets():
    page = 1
    headers = {'User-Agent': random.choice(user_agent)}
    id_set = set()

    while True:
        url = 'https://www.jianshu.com/recommendations/users?utm_source=desktop&utm_medium=index-users&page={0}'.format(
            page)
        print(url)
        resp = requests.get(url, headers=headers)

        result = extract_user_id_set(resp.text)
        if result.issubset(id_set):
            break
        else:
            id_set = id_set.union(result)
        print('--------Page ' + str(page) + ' has been scrawled!---------')
        page += 1
        time.sleep(1)
    return
