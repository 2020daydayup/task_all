import json
from functools import wraps
import os
from src.login import user_admin

def welcome():
    print("欢迎进入功能页面")
    exit()


def yanzheng(func):
    """
    登录验证
    """
    print("启用登录验证")
    @wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            username = input("请输入用户名：").strip()
            if f"{username}.json" not in os.listdir("../data"):
                print("用户名不存在，请先注册")
                user_admin().add_user()
                continue
            passwd = input("请输入密码：").strip()
            with open(f"../data/{username}.json", 'r') as f:
                user_data = json.load(f)
            if passwd == user_data["passwd"]:
                print("登录成功")
                welcome()
            else:
                print("密码错误，请重新输入")
                continue

    return wrapper()

@yanzheng
def login():
    pass
