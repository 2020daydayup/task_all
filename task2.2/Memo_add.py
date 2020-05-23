
import pickle
import os

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

    def __init__(self):
        self.keep = True
        self.file_name = 'db_add.pkl'

    def welcome(self):
        "欢迎方法，功能选择"

        print("欢迎进入51备忘录".center(30,"-"))
        keep = True
        while keep:
            model = input("请选择要执行的操作：按其他键退出\n1：新增\n2：删除\n3：修改\n4：查询\n5：重置\n")
            try:
                select = int(model)
                if select == 1: self.add()
                elif select == 2: self.delete()
                elif select == 4: self.query()
                elif select == 3: self.modify()
                elif select == 5: self.clean()
            except:
                keep = False

    def add(self):
        "新增记录"

        while self.keep:
            task = Memo().task(self.query(2)[0])
            print(task)
            with open(self.file_name, 'ab') as f:
                pickle.dump(task, f)
            print("添加成功")
            self.keep = True if input("请选择是否继续y/n") == 'y' else False

    def delete(self):
        "删除记录"

        memo_all = self.query(2)[1]
        for i in memo_all:
            print(i)

        key = input("请选择要删除的记录id：")
        memo_all.pop(int(key) - 1)
        for i in memo_all:
            print(i)

        with open(self.file_name, 'wb') as f:
            for i in memo_all:
                pickle.dump(i, f)

    def modify(self):
        "修改记录"

        memo_all = self.query(2)

        while self.keep:
            try:
                index = input("请输入要修改记录的id")
                data = input("请输入要修改的结果（eg：date-name-thing）")
                date,name,thing = data.split('-')
                # memo_all = self.query()[1]
                memo_all[1][int(index)-1] = {'date':date, 'name':name, 'thing':thing}

                with open(self.file_name, 'wb') as f:
                    for i in memo_all:
                        pickle.dump(i, f)

                print("修改成功")
                self.query(2)
                self.keep = True if input("请选择是否继续y/n") == 'y'else False

            except:
                print("输入数据格式错误")
                break

    def query(self,model=1):
        "查询记录"

        count = 1 #记录数据量
        num = 0   #给新增的索引
        memo_list = []
        with open(self.file_name,'rb') as f:
            while True:
                try:
                    if model == 1:
                        print(f"记录{count}:" + str(pickle.load(f)))
                    memo_list.append(pickle.load(f))
                    count += 1
                    num += 1
                except:
                    break
        if model == 1:
            print(f"共{count-1}条记录")
        return num, memo_list

    def clean(self):
        "清空备忘录"
        with open(self.file_name, 'r+') as f:
            f.truncate()
        print("清空成功")

if __name__ == '__main__':
    memo_a = MemoAdmin()
    memo_a.welcome()


