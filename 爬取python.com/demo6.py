import os
import requests
from bs4 import BeautifulSoup

base_url = 'https://www.pythontab.com/html/pythonjichu/'
headersvalue = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.8; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}

def get_onepage_url(url):
    url_list = []
    try:
        r = requests.get(url, headers=headersvalue)
        r.raise_for_status()  # 检查请求是否成功
    except requests.exceptions.RequestException as e:
        print('请求失败:', e)
    else:
        soup = BeautifulSoup(r.text, 'html.parser')
        items = soup.select('#catlist li')
        for item in items:
            url1 = item.select('a')[0].attrs['href']
            url_list.append(url1)
    return url_list

def get_article(url):
    try:
        r = requests.get(url, headers=headersvalue)
        r.raise_for_status()  # 检查请求是否成功
    except requests.exceptions.RequestException as e:
        print('请求失败:', e)
    else:
        soup = BeautifulSoup(r.text, 'html.parser')
        title = soup.select('#Article h1')[0].string
        content = soup.select('#Article .content')[0].text
        towrite(title, content)

def towrite(title, content):
    # 替换文件名中的特殊字符
    string = ['?', '*', ':', '"', '<', '>', '\\', '/', '|']
    for i in string:
        if i in title:
            title = title.replace(i, '#')
    # 确保保存文件的目录存在
    path = os.path.join(os.getcwd(), 'Python Basics')
    if not os.path.exists(path):
        os.makedirs(path)
    try:
        with open(os.path.join(path, title + '.txt'), 'w', encoding='utf-8') as f:
            f.write(content.strip())
    except OSError as e:
        print('写文件失败:', e)
    else:
        print('下载完成:', title)

def main():
    for i in range(1, 31):
        if i > 1:
            url = base_url + str(i) + '.html'
        else:
            url = base_url
        url_list = get_onepage_url(url)
        for url1 in url_list:
            get_article(url1)

if __name__ == '__main__':
    main()