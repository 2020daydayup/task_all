import logging
import pickle
import os
import configparser
import pdfkit

class Memo:
    "备忘录基本信息"
    def __init__(self, name='', thing='', date=''):
        self.name = name
        self.thing = thing
        self.date = date

    def task(self,id):
        "录入记录"
        self.date = input('date:')
        self.name = input('name:')
        self.thing = input('thing:')
        one = {'date':self.date,'name':self.name,'thing':self.thing}
        return one

class MemoAdmin():
    "备忘录主类，作为主体程序，管理Memo类构成了列表，进行Memo的增删改查清空"

    def __init__(self, filename):
        self.file_name = filename


    def welcome(self, username):
        "欢迎方法，功能选择"

        print(f"欢迎{username}")
        keep = True
        while keep:
            model = input("请选择要执行的操作：按其他键退出\n1：新增\n2：删除\n3：修改\n4：查询\n5：下载\n6：重置\n")
            try:
                select = int(model)
                if   select == 1: self.add(username)
                elif select == 2: self.delete(username=username)
                elif select == 4: self.query(username=username)
                elif select == 3: self.modify(username=username)
                elif select == 5:
                    if self.query(username=username)[1]:
                        self.download(username)
                    else:
                        return self.welcome(username)
                elif select == 6: self.clean(username=username)
            except:
                keep = False

    def add(self, username):
        "新增记录"

        print("进入新增页面")
        keep = True
        while keep:
            print("进入新增循环")
            task = Memo().task(self.query(2,username=username)[0])
            print(task)
            with open(self.file_name, 'ab') as f:
                pickle.dump(task, f)
            print("添加成功")
            loglog().info(f'{username}添加记录：{task}')
            keep = True if input("请选择是否继续y/n") == 'y' else False

    def delete(self,username):
        "删除记录"

        print("进入删除页面")
        memo_all = self.query(2, username=username)[1]
        index = 1
        for memo in memo_all:
            print(f'{index}:{memo}')
            index += 1

        key = input("请选择要删除的记录id：")
        memo_all.pop(int(key) - 1)
        loglog().info(f'{username}删除记录：{memo_all[int(key) - 1]}')
        for i in memo_all:
            print(i)

        with open(self.file_name, 'wb') as f:
            for i in memo_all:
                pickle.dump(i, f)

    def modify(self, username):
        "修改记录"

        print("进入修改页面")
        memo_all = self.query(2, username=username)[1]
        index = 1
        for memo in memo_all:
            print(f'{index}:{memo}')
            index += 1
        keep = True
        while keep:
            try:
                index = input("请输入要修改记录的id")
                data = input("请输入要修改的结果（eg：date-name-thing）")
                date,name,thing = data.split('-')
                memo_all[1][int(index)-1] = {'date':date, 'name':name, 'thing':thing}

                with open(self.file_name, 'wb') as f:
                    for i in memo_all:
                        pickle.dump(i, f)

                print("修改成功")
                loglog().info(f'{username}删除记录：{memo_all[1][int(index)-1]}')
                self.query(2)
                keep = True if input("请选择是否继续y/n") == 'y'else False

            except:
                print("输入数据格式错误")
                loglog().info(f'{username}删除记录操作不对')
                break

    def query(self,model=1,username=''):
        "查询记录"

        count = 1 #记录数据量
        num = 0   #给新增的索引
        memo_list = []
        if os.path.getsize(f'data/{username}.pkl'):
            with open(self.file_name,'rb') as f:
                while True:
                    try:
                        memo_list.append(pickle.load(f))
                        count += 1
                        num += 1
                    except:
                        break
        if model == 1:
            print(f"共{count-1}条记录")
            loglog().info(f'{username}查询记录')
            index = 1
            for memo in memo_list:
                print(f'{index}:{memo}')
                index += 1

        return num, memo_list

    def download(self, username):
        "生成pdf"
        content = """<head><meta charset='UTF-8'></head>
                        <h1 align='center'>待办事项</h1></br>
                 """
        memo_all = self.query(2, username=username)[1]

        for memo in memo_all:
            content = content + str(memo) + '<br>'
        config = pdfkit.configuration(wkhtmltopdf=r"config\wkhtmltopdf.exe")
        pdfkit.from_string(content, f"downloads/{username}.pdf", configuration=config)
        print("下载成功")
        loglog().info(f'{username}下载记录')

    def clean(self,username):
        "清空备忘录"
        with open(self.file_name, 'r+') as f:
            f.truncate()
        print("清空成功")
        loglog().info(f'{username}清空记录')

class Register():
    "首页，包含登录、注册"

    def get_users(self):
        "获取所有用户"
        user_dict = {}
        users_file = r'data/users.pkl'
        # 读取已存在的用户信息，用作重复性判断
        if os.path.exists(users_file):
            if os.path.getsize(users_file):
                with open(users_file, 'rb') as f_r:
                    user_dict = pickle.load(f_r)

        else:
            f = open(users_file, 'w')
            f.close()
        return user_dict

    def welcome(self):
        "备忘录首页"
        user_dict = self.get_users()
        print("欢迎进入51备忘录".center(30, "-"))
        select = input("请选择\n1：登录，2：注册，其他键退出")
        if int(select) == 1:
            self.login(user_dict)
        elif int(select) == 2:
            self.verify()
        else:
            quit()

    def verify(self):
        "注册验证，已存在则提示不允许重复，不存在则新增，新增成功后返回登录模块"

        print("已经进入注册页面".center(30, "-"))
        user_dict = self.get_users()
        username = input("请输入用户名：")
        password = input("请输入密码：")

        #注册验证，注册成功后创建用户数据文件
        if username in user_dict.keys():
             print("用户名已存在")

        else:
            user_dict[username] = password
            with open(r'data/users.pkl', 'wb') as f_w:
                pickle.dump(user_dict, f_w)
            # 创建用户文件
            f = open(f'data/{username}.pkl' , 'wb')
            f.close()
            print("注册成功")
            loglog().info(f'{username}注册成功')


            #添加到配置文件去
            config = configparser.ConfigParser()
            config[username] = {'filename':f'{username}.pkl', 'datapath':os.path.abspath('.')+'/data'}
            with open(r'config/config.properties', 'w') as f_c:
                config.write(f_c)

            #进入登录页面
            self.login(self.get_users())

    def login(self, user_dict):
        "登录判断"

        print('登录页面'.center(30, "-"))
        username = input("请输入用户名：")
        password = input("请输入密码：")
        if username in user_dict.keys():
            if user_dict[username] == password:
                loglog().info(f'{username}登录成功')
                MemoAdmin(f"data/{username}.pkl").welcome(username)
            else:
                print("密码错误，请重新输入")
                return self.login(user_dict)
        else:
            print("用户名不存在，请先注册")
            self.verify()

def loglog():
    # 创建 logger对象
    level = logging.DEBUG
    log_file = 'logs/memo.log'
    logger_name = 'DE8UG-LOG'
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)  # 添加等级

    # 创建控制台 console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # 创建文件 handler
    fh = logging.FileHandler(filename=log_file, encoding='utf-8')

    # 创建 formatter
    formatter = logging.Formatter('%(asctime)s [line:%(lineno)d] : %(levelname)s %(message)s')

    # 添加 formatter
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 把 ch， fh 添加到 logger
    # logger.addHandler(ch)
    logger.addHandler(fh)

    return logger

def qingk(file):
    "清空文件，测试用"
    with open(file,'w+') as f:
        f.truncate()

def deletef(file):
    "删除文件，测试用"
    os.remove(file)


if __name__ == '__main__':
    # qingk('users.pkl')
    # if os.path.exists("1.pdf"):
    #     deletef('1.pdf')
    r = Register()
    r.welcome()

