import os, pyminizip

path = []
spath = []

def zip_it(file_name, password):
    # 原文件路径
    # 压缩文件解压后的文件夹名称
    # zip文件名
    # 密码
    # 速度 compress_level(int) between 1 to 9, 1 (more fast) <---> 9 (more compress) or 0 (default)
    pyminizip.compress_multiple(path, spath, (file_name + '.zip'), password, 0)

def get_dir_constents(name, sPath):
    global path
    #列出当前路径下的所有文件夹和文件　并进行遍历
    for schild in os.listdir(sPath):
        #拼接地址
        sChildPath = os.path.join(sPath, schild)
        #判断当前遍历到的是文件还是文件夹
        if os.path.isdir(sChildPath):
            #再次递归调用
            get_dir_constents(name, sChildPath)
        else:
            if '.DS_Store' not in schild:
                path.append(sChildPath)
                new_spath = sPath.split(name)[-1]       # 此处需要一个分割名，用来辨别路径的分割位置；如果没有这一行，压缩文件中则会出现根路径
                spath.append(new_spath)
    