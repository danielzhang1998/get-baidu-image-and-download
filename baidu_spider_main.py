import requests, pyminizip, sys
from urllib.parse import urlencode
import spider, packing, time, random, os
import urllib.request as u_request
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk as Image_post

file_name = ''  # 用来获取母文件夹名称
current_dir = ''
currently_page = 0 # 当前是下载第几张
name = ''
pages = ''
TOTAL_DOWNLOADS = 0

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def save(new_pic):
    global currently_page
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

        currently_page += 1
        update_it(currently_page, TOTAL_DOWNLOADS)
    print('fail:' + str(len(new_pic) - count))
    if len(new_pic) - count :
        print('the reason why fail to download might be the file type is undistinguishable or the file already exists!')

def make_folder(file_dir):
    global current_dir
    os.mkdir(file_dir)
    os.chdir(file_dir)
    current_dir = os.getcwd()

def update_it(each, TOTAL_DOWNLOADS):
        pr = (each / TOTAL_DOWNLOADS * 100)
        canvas.coords(rect, (0, 20, pr * 10, 0))
        percentage.set(each)
        canvas.itemconfig(bar, text = str(float("{:.2f}".format(pr))) + '%')
        if pr > 55:
            canvas.itemconfig(bar, fill = 'white')
        window.update()

def start():
    name = new_concept.get()
    pages = new_image_num.get()
    parent_folder1 = new_parent_folder.get()
    zip_pwd1 = new_zip_pwd.get()
    zip_pwd2 = new_zip_pwd_1.get()
    if name == '':
        messagebox.showerror("Error!", "搜索的内容不能为空!")
    else:
        if pages == '':
            messagebox.showerror("Error!", "输入值不能为空,请重新输入您想要下载的页数(数值需大于 30)!")
        elif (not pages.isdigit()) or (pages.isdigit() and int(pages) <= 30):
            messagebox.showerror("Error!", "输入不合法,请重新输入您想要下载的页数(数值需大于 30)!")
        else:
            if zip_pwd1 == zip_pwd2:
                try:
                    make_folder(parent_folder1)
                    main(name, pages, parent_folder1, zip_pwd1)
                except FileExistsError:
                    messagebox.showerror("Error!", "文件已经存在，请重新输入新的文件名!")
            else:
                messagebox.showerror("Error!", "两次所输入的密码有所不同，请重新输入!")


def reset():
    new_concept.set('')
    new_image_num.set('')
    new_parent_folder.set('')
    new_zip_pwd.set('')
    new_zip_pwd_1.set('')

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

window = tk.Tk()
window.title('Downloading...')
window.geometry('1000x800')

new_concept = tk.StringVar()
new_image_num = tk.StringVar()
new_parent_folder = tk.StringVar()
new_zip_pwd = tk.StringVar()
new_zip_pwd_1 = tk.StringVar()

percentage = tk.StringVar()



photo = Image_post.PhotoImage(file = resource_path("title_image.jpeg"))
imgLabel = tk.Label(window, image = photo)
imgLabel.place(x = 450, y = 45)

tk.Label(window, text = '请输入你想搜索的内容:', font=('microsoft yahei', 12, 'bold')).place(x = 205, y = 170)
concept = tk.Entry(window, show = None, textvariable = new_concept, width = 30, bg = 'whitesmoke')
concept.place(x = 430, y = 170)

tk.Label(window, text = '请输入你想获取的图片数量:', font=('microsoft yahei', 12, 'bold')).place(x = 205, y = 240)
image_get_num = tk.Entry(window, show = None, textvariable = new_image_num, width = 30, bg = 'whitesmoke')
image_get_num.place(x = 430, y = 240)

tk.Label(window, text = '请输入图片放置的主文件夹:', font=('microsoft yahei', 12, 'bold')).place(x = 205, y = 310)
parent_folder = tk.Entry(window, show = None, textvariable = new_parent_folder, width = 30, bg = 'whitesmoke')
parent_folder.place(x = 430, y = 310)

tk.Label(window, text = '请设置 zip 文件的密码:', font=('microsoft yahei', 12, 'bold')).place(x = 205, y = 380)
zip_pwd = tk.Entry(window, show = '*', textvariable = new_zip_pwd, width = 30, bg = 'whitesmoke')
zip_pwd.place(x = 430, y = 380)

tk.Label(window, text = '请再次输入 zip 文件的密码:', font=('microsoft yahei', 12, 'bold')).place(x = 205, y = 450)
zip_pwd_1 = tk.Entry(window, show = '*', textvariable = new_zip_pwd_1, width = 30, bg = 'whitesmoke')
zip_pwd_1.place(x = 430, y = 450)

b1 = tk.Button(window, text = 'start it', width = 15, height = 2, command = start)
b1.place(x = 250, y = 520)

b2 = tk.Button(window, text = 'reset all', width = 15, height = 2, command = reset)
b2.place(x = 500, y = 520)

canvas = tk.Canvas(window, bg = 'lightgrey', height = 20, width = 1000)
canvas.pack(side = 'bottom')

rect = canvas.create_rectangle(0, 20, 0, 0, fill = '#32CD32')

bar = canvas.create_text(500, 12, text = str(percentage.get()), fill = 'black')

full_set = set()
count = 0   # 获取了几次图片

def main(name, pages, file_dir, password):
    percentage.set('0')
    global TOTAL_DOWNLOADS
    TOTAL_DOWNLOADS = (int(pages)  - 1)// 30 * 30
    global count
    for each in range(30, int(pages), 30):
        if count == 0 or count % 10 == 0:
            if count % 10 == 0 and count != 0:
                os.chdir('..')
            elif count == 0:
                file_name = file_dir
            folder_number = str(count // 10)
            os.mkdir(file_dir + folder_number)
            os.chdir(file_dir + folder_number)
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
    for each in os.listdir('.'):
        packing.path = []  # 一定要重置，否则 list 将会包含之前的文件夹里的内容一并压缩
        packing.spath = []  # 一定要重置，否则 list 将会包含之前的文件夹里的内容一并压缩
        if '.DS_Store' not in each:
            print(each)
            print(os.getcwd() + '/' + each)
            packing.get_dir_constents(each, os.getcwd() + '/' + each)
            packing.zip_it(each, password)

    messagebox.showinfo(title='Finished', message = 'the file store at:' + os.getcwd())
    window.destroy()

window.mainloop()