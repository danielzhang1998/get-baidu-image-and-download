import json, requests, ssl, re

headers = {
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
'Accept': 'text/html'
}

# 当 json 不好用时
def open_url(url):
    # encoding: utf-8
    ssl._create_default_https_context = ssl._create_unverified_context
    html = requests.get(url,headers=headers).text # 获取url内容
    return html

def get_image(url):
    html = open_url(url)
    m = r'thumbURL":".+?"'
    match = re.findall(m, html)
    for each in range(len(match)):
        match[each] = match[each].split('"')[-2]
    return match

# 优先使用 json 进行加载
def get_image_link(url):
    link_list = []
    res = ''
    ssl._create_default_https_context = ssl._create_unverified_context
    r = requests.get(url, headers=headers).text
    try:
        res = json.loads(r)['data']
    except json.JSONDecodeError:
        link_list = get_image(url)
    for each in res:
        try:
            link_list.append(each['thumbURL'])
        except KeyError:
            pass
    return link_list