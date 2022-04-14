import os
import time


def info(name1):
    print("\n\n---------以下信息由系统自动生成---------")
    print("执行时间：" + time.strftime("%Y-%m-%d %H:%M:%S"))
    print("执行耗时：" + str(int(time.time() * 1000 - startTime * 1000)) + "ms")
    print("程序作者：" + name1)
    print("测试台作者：ShirakawaTyu(方律奔)")
    print("测试台版本：1.0")


name = "X07.方律奔"
package = "com.shirakawatyu.test."
path = os.getcwd()
print("程序列表：")
py = os.listdir(path + "\\test")
for i in py:
    if ".py" in str(i):
        print(str(i))
print("请输入需要测试的程序：")
exe = input().strip().replace(".py", "")
print()
startTime = time.time()
try:
    __import__(package + exe)
except ModuleNotFoundError:
    print("该程序不存在！")
info(name)
