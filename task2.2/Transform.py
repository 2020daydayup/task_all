import re

class  LengthConversion:
    "长度转换"
    value = 0

    def __init__(self,value):
        self.__rate__ = 0.9144
        self.value = value

    def m2yd(self, value):
        "米转换成码"
        result = round(value / self.__rate__, 4)
        print(f"{self.value} = {str(result)}码(yd)")

    def yd2m(self,value):
        "码转换成米"
        result = round(value * self.__rate__, 4)
        print(f"{self.value} = {str(result)}米(m)")

    def main_exption(self):
        "异常数据处理"
        re_data = r'^(\d+|\d+\.\d+)(yd|m)'
        re_num = r'\d+\.?\d*'
        if re.match(re_data, self.value):
            value = float((re.findall(re_num,self.value))[0])
            self.judge(value)
        else:
            print("输入数据错误："+self.value)

    def judge(self, value):
        "判断输入长度单位"
        if "yd" in self.value:
            self.yd2m(value)
        else:
            self.m2yd(value)

class ExchangeRate:
    "汇率转换类"

    value = 0

    def __init__(self,value):
        self.__exchange_rate__ = 6.9298
        self.value = value

    def cny2usd(self, value):
        "人民币转换成美元"
        result = round(value / self.__exchange_rate__, 4)
        print(f"{self.value} = ${str(result)}")

    def usd2cny(self,value):
        "美元转换成人民币"
        result = round(value * self.__exchange_rate__, 4)
        print(f"{self.value} = ￥{str(result)}")

    def main_exption(self):
        "异常数据处理"
        re_data = r'^\$|￥(\d+|\d+\.\d+)'
        if re.match(re_data, self.value):
            value = float((self.value)[1:])
            self.judge(value)
        else:
            print("输入数据错误："+self.value)
    def judge(self, value):
        "判断输入币种"
        if "￥" in self.value:
            self.cny2usd(value)
        else:
            self.usd2cny(value)

class  TemperatureConverter:
    "温度转换"
    value = 0

    def __init__(self,value):
        self.__rate__ = 1.8
        self.value = value

    def centigrade2f(self, value):
        "摄氏度转换为华氏度"
        result = round(value * (9 / 5)+ 32, 4)
        print(f"{self.value} = {str(result)}华氏度(°F)")

    def f2centigrade(self,value):
        "华氏度转换为摄氏度"
        result = round((value - 32) * (5/9), 4)
        print(f"{self.value} = {str(result)}摄氏度(°C)")

    def main_exption(self):
        "异常数据处理及转换入口"
        re_data = r'^(\d+|\d+\.\d+)(f|c)'
        re_num = r'\d+\.?\d*'
        if re.match(re_data, self.value):
            value = float((re.findall(re_num,self.value))[0])
            self.judge(value)
        else:
            print("输入数据错误："+self.value)

    def judge(self, value):
        "判断输入温度单位，调用不同的温度转换方法"
        if "f" in self.value:
            self.f2centigrade(value)
        else:
            self.centigrade2f(value)

class Transfer:
    "转换器主类，输入及判断"

    def mian_input(self):
        "程序入口"

        keep = True
        while (keep):
            print("'t'代表温度：'1c'表示1摄氏度，'1f'表示1华氏温度")
            print("'len'代表长度：'1m'表示1米，'1yd'表示1英码")
            print("'e'代表汇率：'￥1'表示1人民币，'$1'表示1美元")
            select = input("请选择单位类型（t/len/e）：")

            if select.lower() == 't':
                value = input("请输入要转换的数值：")
                TemperatureConverter(value).main_exption()
                keep = input("是否继续（y/n）：") == 'y'

            elif select.lower() == 'len':
                value = input("请输入要转换的数值：")
                LengthConversion(value).main_exption()
                keep = input("是否继续（y/n）：") == 'y'

            elif select.lower() == 'e':
                value = input("请输入要转换的数值：")
                ExchangeRate(value).main_exption()
                keep = input("是否继续（y/n）：") == 'y'

            else:
                print("数据格式错误")
                keep = input("是否继续（y/n）：") == 'y'

if __name__ == '__main__':
    Transfer().mian_input()