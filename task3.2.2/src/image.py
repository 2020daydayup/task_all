import configparser
from PIL import Image
import pandas as pd
import os
from src.getlog import get_log

class ImageUtils():
    "图片处理类"
    def __init__(self):
        """初始化方法，1、必须传入操作模式，分旋、裁剪
                    2、获取配置文件中的图片路径
                    3、获取配置文件中的保存excel的路径
        """
        # self.handle = handle
        config = configparser.ConfigParser()
        config.read("../config/pic.config")
        self.pic_path = dict(config.items('path'))['pic_path']
        self.data_path = dict(config.items('path'))['data_path']

    def get_all_path(self, open_file_path):
        "获取文件夹下所有文件的相对路径及文件名称"
        rootdir = open_file_path
        path_list = []
        file_list = []
        file_dict = {}
        list = os.listdir(rootdir)
        for i in range(0, len(list)):
            com_path = os.path.join(rootdir, list[i])
            if os.path.isfile(com_path) and (os.path.splitext(com_path)[1] in ('.png', '.jpg', '.bam')):
                path_list.append(com_path)
                fsize = self.get_file_size(com_path)
                file_dict[com_path] = fsize
                file_list.append(list[i])
            if os.path.isdir(com_path):
                path_list.extend(self.get_all_path(com_path)[0])

        return path_list, file_list, file_dict

    def get_file_size(self, filepath):
        "获取文件大小"
        fsize = os.path.getsize(filepath)
        if fsize > 1024*1024:
            fsize = fsize/float(1024 * 1024)
            fsize = str(round(fsize, 2)) + 'M'
        else:
            fsize = fsize / float(1024)
            fsize = str(round(fsize, 2)) + 'K'
        return fsize

    def save_pics(self):
        "根据配置文件中的图片路径，保存所有（png、jpg、bmp）文件到指定路径下的excel里"
        pic_path_boole = os.path.exists(self.pic_path)
        data_path_boole = os.path.exists(self.data_path)
        dic1 = {}
        if pic_path_boole and data_path_boole:
            data = self.get_all_path(self.pic_path)
            dic1['大小'] = list(data[2].values())
            dic1["名称"] = data[1]
            df = pd.DataFrame(dic1)
            df.to_excel('../datas/test.xlsx', index=False)
        get_log().loglog().info("生成excel成功，路径为：datas/test.xlsx")

    def rotate_pic(self,picname, angle):
        "旋转图片方法，传入文件路径，角度"
        im = Image.open(os.path.join(self.pic_path,picname))
        out = im.rotate(angle)
        newname = os.path.join(self.pic_path, f"{str(angle)}_{picname}")
        get_log().loglog().info(f"图片旋转成功，路径为：{newname}，参数为：{angle}度")
        out.save(newname)

    def cut_pic(self, picname, box):
        "裁剪图片方法，传入文件路径"
        # box = eval(box)
        img = Image.open(os.path.join(self.pic_path,picname))
        cropped = img.crop(box)  # (left, upper, right, lower)
        s = ""  #box[0]+'_'+box[1]+'_'+box[2]+'_'+box[3]+'_'
        for i in box:
            s += str(i) + '_'
        newname = os.path.join(self.pic_path, f"cut_{s}{picname}")
        cropped.save(newname)
        get_log().loglog().info(f"图片裁剪成功，路径为：{newname}，参数为：{box}")

class selectUtil():
    "功能选择类，根据选择调用对应的图片处理方法"
    def __init__(self):
        self.iutil = ImageUtils()

    def welcome(self):
        "欢迎方法"
        while True:
            select = input("请选择操作模式\n1：生成图片路径excel\n2：旋转图片\n3：裁剪图片\n其他键退出").strip()
            try:
                select = int(select)
                if select == 1:
                    self.iutil.save_pics()
                elif select == 2 :
                    picname = input("请输入文件名称：").strip()
                    angle = input("请输入选择角度：").strip()
                    angle = int(angle)
                    self.iutil.rotate_pic(picname=picname, angle=angle)
                elif select == 3:
                    picname = input("请输入文件名称：").strip()
                    box = input("请输入裁剪规则（4位元组），例(1,2,3,4)：").strip()
                    # print("1111111"+str(box))
                    box = eval(box)
                    # print(box)
                    self.iutil.cut_pic(picname=picname, box=box)
                else: break
            except BaseException as e:
                get_log().loglog().error(e)
                print(f"数据格式错误:{e}")

if __name__ == '__main__':
    selectUtil().welcome()


