import os
import codecs


def write_append_file_crawled_user(file_name, content):
    with codecs.open(file_name, 'a', encoding='utf-8') as f:
        f.write(content)
        f.write('\n')
