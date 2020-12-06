from lxml import html
import os
import codecs
import requests
from bs4 import BeautifulSoup
from jianshu_scrawler.path.path_file import get_files_path_userid


def ReadDataFromHtmlFile(userid, articleid):
    file_dir = get_files_path_userid(userid)
    for filename in os.listdir(file_dir):
        if filename.endswith('html'):
            file_path = os.path.join(file_dir, filename)
            article_id = filename.replace('.html', '')
            if article_id != articleid:
                continue
            url = 'http://www.jianshu.com/p/{0}'.format(article_id)
            # html_content = codecs.open(file_path, 'r', encoding='utf-8')
            f = open(file_path, "rb")
            content = f.read().decode('utf-8')
            p = html.etree.HTML(content)
            soup = BeautifulSoup(content, 'lxml')
            lists = p.xpath('//div[@class="_3VRLsv"]/div/text()')
            print(lists)
            title = p.xpath('//h1[@class="_1RuRku"]/text()')
            print(title)
            author = p.xpath('//div[@class="_3U4Smb"]')
            print(author)
            uptime = p.xpath('//div[@class="s-dsoj"]/time/text()')
            print(uptime)
            articletitle = soup.find('h1', class_='_1RuRku').text
            print(articletitle)
            author = soup.find_all('a', target='_blank')
            print(author)

ReadDataFromHtmlFile('14ff9312d3d3', 'bb8d2838d314')
