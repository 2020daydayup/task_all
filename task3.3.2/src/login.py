import json
import src.logUtil as log
import os
import src.autoOffice as office
import src.analysis as als
import src.aaa as llogin

class user_admin():
    "用户管理类，处理用户登录、注册等功能"

    def __init__(self):
        pass

    def add_user(self):
        "注册、新增用户"
        print("启用注册功能")
        while True:
            username = input("请输入用户名：").strip()
            if username+'.json' in os.listdir("../data"):
                print("用户名已存在，请重新输入")
                continue
            passwd = input("请输入密码：").strip()
            context = {"username": username, "passwd":passwd, "status":0, "is_delete":0, "operation" : []}
            with open(f"../data/{username}.json", 'w') as u_f:
                json.dump(context, u_f, indent=2)
            print("注册成功")
            log.get_log().loglog().info(f"用户注册账号成功,用户信息为：{context}")
            llogin.login()

    def login(self, username):
        "登录"
        if username + '.json' not in os.listdir("../data"):
            print("用户名不存在，请重新输入")
            return self.login(username)
        while True:
            passwd = input("请输入密码：").strip()
            with open(f"../data/{username}.json", 'r') as u_f:
                user_data = json.load(u_f)
            if passwd == user_data['passwd']:
                print("登录成功")
                break
            else:
                print("密码错误，请重新输入")
                continue

    def rgant(self):
        "赋权"
        pass

    def welcome(self):
        "系统首页"

        print("欢迎进入数据处理系统".center(50,'-'))
        while True:
            try:
                select = int(input("1：登录\n2：注册\n其他退出").strip())
                if select == 1: self.login(input("请输入用户名：").strip())
                if select == 2: self.add_user()
                else: quit()
            except ValueError as e:
                log.get_log().loglog().error("数据格式错误")
                print(e)
                continue

class user_operation():
    "功能选择模块"
    def __init__(self, username, operation):
        self.username = username
        self.operation = operation

    def fun_sel(self):
        ""
        if self.operation == []:
            print("您没有任何权限，请联系管理员加权限")
        else:
            play = input(f"{self.operation}\n请选择对应的操作：").strip()
            if play == "office": office.analysis().test_methon()
            elif play == "analysis" : als.analysis().test_methon()


if __name__ == '__main__':
    ua = user_admin()
    ua.welcome()
