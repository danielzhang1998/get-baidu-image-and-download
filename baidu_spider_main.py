import requests, pyminizip
from urllib.parse import urlencode
import spider, packing, time, random, os
import urllib.request as u_request

file_name = ''  # 用来获取母文件夹名称
current_dir = ''

def save(new_pic):
    count = 0
    for each in new_pic:
        if each not in full_set:
            try:
                req = u_request.Request(each, headers = spider.headers)
                response = u_request.urlopen(req)
                cat_image = response.read()
                filename = each.split('/')[-1]
                with open(filename,'wb') as f:
                    f.write(cat_image)
                print(each)
            except OSError as error:
                print(error)
                continue
            except ValueError as error:
                print(error)
                continue
            sleep_time = round(random.uniform(0,0.05),5)
            time.sleep(sleep_time)

            count += 1
            print("successful: " + str(count) + '/' + str(len(new_pic)))
    print('fail:' + str(len(new_pic) - count))
    if len(new_pic) - count :
        print('the reason why fail to download might be the file type is undistinguishable or the file already exists!')

def make_folder():
    global file_dir
    global current_dir
    try:
        file_dir = input("请输入想要存储的目标文件夹：\n")
        os.mkdir(file_dir)
        os.chdir(file_dir)
        current_dir = os.getcwd()
    except FileExistsError:
        print('the folder already exists, please enter a new name!')
        make_folder()

name = input("请输入您需要爬取的图片信息：\n")
pages = input("请输入您想要下载的页数：\n")

while (not pages.isdigit()) or (pages.isdigit() and int(pages) <= 30):
    pages = input("输入不合法,请重新输入您想要下载的页数：\n")

make_folder()

bef_url = 'https://image.baidu.com/search/index?'

data = {
    'tn': 'resultjson_com',
    'logid': '7786358177497367672',
    'ipn': 'rj',
    'ct': '201326592',
    'is': '',
    'fp': 'result',
    'queryWord': '',
    'cl': '2',
    'lm': '-1',
    'ie': 'utf-8',
    'oe': 'utf-8',
    'adpicid': '',
    'st': '-1',
    'z': '',
    'ic': '',
    'hd': '',
    'latest': '',
    'copyright': '',
    'word': '',
    's': '',
    'se': '',
    'tab': '',
    'width': '',
    'height': '',
    'face': '0',
    'istype': '2',
    'qc': '',
    'nc': '1',
    'fr': '',
    'expermode': '',
    'force': '',
    'pn': '0',
    'rn': '30',
    'gsm': '1e',
    '1561022599290': '' # 时间戳
}


full_set = set()
count = 0   # 获取了几次图片
for each in range(30, int(pages), 30):
    if count == 0 or count % 20 == 0:
        if count % 20 == 0 and count != 0:
            os.chdir('..')
        elif count == 0:
            file_name = file_dir
        make_folder()
    millis = int(round(time.time() * 1000)) # 生成时间戳
    data['word'] = name
    data['queryWord'] = name
    data['pn'] = each   # 翻页
    data.popitem()  # 去掉最后一个元素，即旧的时间戳
    data[millis] = ''   # 添加新的时间戳
    hex_num = hex(each)[2:]
    data['gsm'] = hex_num
    url = bef_url + urlencode(data)
    image_list = spider.get_image_link(url)
    save(image_list) # 存储 image
    for each in image_list:
        full_set.add(each)  # 当前一共下载了多少页
    print('total pages:' + str(len(full_set)))
    count += 1
    sleep_time = round(random.uniform(0.5,2),4) # 休眠
    time.sleep(sleep_time)

os.chdir('..')
password = input('请设置 zip 文件的密码!\n')
for each in os.listdir('.'):
    packing.path = []  # 一定要重置，否则 list 将会包含之前的文件夹里的内容一并压缩
    packing.spath = []  # 一定要重置，否则 list 将会包含之前的文件夹里的内容一并压缩
    if '.DS_Store' not in each:
        print(each)
        print(os.getcwd() + '/' + each)
        packing.get_dir_constents(each, os.getcwd() + '/' + each)
        packing.zip_it(each, password)