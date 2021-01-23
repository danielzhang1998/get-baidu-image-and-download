import json, requests, ssl

headers = {
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
'Accept': 'text/html'
}

def get_image_link(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    r = requests.get(url, headers=headers).text
    res = json.loads(r)['data']
    link_list = []
    for each in res:
        try:
            link_list.append(each['thumbURL'])
        except KeyError:
            pass
    return link_list

if __name__ == '__main__':
    url = input('enter\n')
    get_image_link(url)