import os
import codecs
from jianshu_scrawler.spiders.scrawl_user_list import get_user_path, get_article_id_sets
from jianshu_scrawler.database.create_jianshufull_index_es import CreateIndices
from jianshu_scrawler.path.path_file import get_user_path_file, get_crawleduser_path_file
from jianshu_scrawler.spiders.scrawl_content_by_user import download_articles_userid
from jianshu_scrawler.logs.write_config import write_append_file_crawled_user
from jianshu_scrawler.database.writedata_jianshufull_es import WriteData_In_Elastic


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def get_users_list():
    users = [
        '',
    ]
    user_len = 0
    file_path = get_user_path_file('user.txt')
    if not os.path.exists(file_path):
        print('This is no file ' + file_path)
    else:
        f = open(file_path)
        line = f.readline()
        while line:
            users.append(line.replace('\n', ''))
            line = f.readline()
        user_len = len(users) - 1
        print('There are ' + str(user_len) + ' users need to crawl as below: ')
        print(users)
        f.close()
    return users


def crawl_users_list_file():
    user_file = get_user_path_file('user.txt')
    if os.path.exists(user_file):
        print('user.txt has been existed!')
        return
    get_article_id_sets()


def crawl_contnet_file_by_users(users):
    file_crawled = get_user_path_file('crawled_user.txt')
    for user_id in users:
        if len(user_id) == 0:
            continue
        download_articles_userid(user_id)
        write_append_file_crawled_user(file_crawled, user_id)

        # 写入指定user ID的数据到ES数据库中
        WriteData_In_Elastic(user_id)





def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')z
    # 首先如果user清单不存在，则爬取用户清单，并存入到user.txt中
    crawl_users_list_file()

    # 创建article_full索引，如果存在该索引，不会重复创建
    CreateIndices('article_full')

    # 获取用户ID集合
    users = get_users_list()

    # 爬取用户ID集合中的内容
    crawl_contnet_file_by_users(users)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
