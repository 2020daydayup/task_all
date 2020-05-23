import pickle
class Memo:
    def __init__(self, name='', thing='', date=''):
        self._id = 0
        self.name = name
        self.thing = thing
        self.date = date

    def talk(self):
        "添加数据"

        self._id += 1
        self.name = input('name:')
        self.thing = input('thing:')
        self.date = input('date:')
        one = {'id':self.id,'name':self.name,'thing':self.thing,'date':self.date}
        return one

    @property
    def id(self): # 只读
        return self._id

class MemoAdmin:
    """管理记录"""

    def __init__(self):   # 初始化数据
        self.dir =  {'1': 'Add',
           '2': 'Dele',
           '3': 'Modify',
           '4': 'Query',
           '5': 'Save',
           '6': 'Load'
           }
        self.memo_list = []
        self.memo = Memo()

    def welcome(self,model=1):
        "首页"

        if model == 1:
            print('欢迎使用51备忘录'.center(50,'-'))
        for k,v in self.dir.items():
            print(f'{k}:{v}')         # 打印选择选项
        t = input('请选择你的操作选项 (示例 1)：')

        while True:
            L = Memo()
            if t == '1': self.add()
            elif t == '2': self.dele()
            elif t == '3': self.modify()
            elif t == '4': self.query()
            elif t == '5': self.save()
            elif t == '6': self.load()
            elif t == 'q' :
                print("再见")
                exit()
            else:
                print('结束')

    def add(self):
        "增加方法"

        self.memo_list.append(self.memo.talk())
        self.query()
        print('增加成功')

        self.welcome(2)

    def dele(self):    # 删除方法
        temp = input('请选择你将要删除的记录（示例 1或者2或者3 ）:')
        self.memo_list.pop(int(temp)-1)
        print('删除成功')
        self.query()
        self.welcome(2)
    def modify(self):   # 修改方法
        temp1 = input('请输入你要修改的记录（示例 1或者2或者3）:')
        temp2 = input(f'你要修改的记录是{self.memo_list[int(temp1)-1]}\n请输入要修改的值（示例：name:zhangsan）:')
        temp3 = temp2.split(':')
        self.memo_list[int(temp1)-1][temp3[0]] = temp3[1]   # 列表中找出嵌套的字典key和value
        print('修改成功')
        self.query()
        self.welcome(2)
    def save(self):
        "数据保存在文件内"

        with open('db.pkl','wb') as f:
            f.write(pickle.dumps(self.memo_list))
            print('保存成功')
        self.welcome(2)

    def load(self):
        "下载文件"
        with open('db.pkl','rb') as f:
            data = pickle.loads(f.read())
            print(data)
            print('下载成功')
        self.welcome(2)

    def query(self):
        "查询所有数据"
        i = 0
        for k in self.memo_list:
            i += 1
            print(f'项目{i}{k}')
        self.welcome(2)

if __name__ == '__main__':

    R = MemoAdmin().welcome()