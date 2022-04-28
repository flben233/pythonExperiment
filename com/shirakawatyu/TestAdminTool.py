import datetime
import os
import sys
import time
import pygame

po = ""


# 用于输出相关信息的方法
def info(name1):
    print("\n\n---------以下信息由系统自动生成---------")
    print("执行时间：" + time.strftime("%Y-%m-%d %H:%M:%S"))
    print("执行耗时：" + str(int((datetime.datetime.now() - startTime).total_seconds() * 1000)) + "ms")
    print("程序作者：" + name1)
    print("测试台作者：ShirakawaTyu(方律奔)")
    print("测试台版本：1.2")
    return "\n\n---------以下信息由系统自动生成---------\n" + "执行时间：" + time.strftime(
        "%Y-%m-%d %H:%M:%S") + "\n执行耗时：" + str(int((datetime.datetime.now() - startTime).total_seconds() * 1000)) + "ms" + "\n程序作者：" + name1 + "\n测试台作者：ShirakawaTyu(方律奔)" + "\n测试台版本：1.0"


# 用于截获print()输出的类
class LoggerPrint(object):
    def __init__(self, stream=sys.stdout):
        self.terminal = stream
        # self.log = open(filename, 'a')

    def write(self, message):
        self.terminal.write(message)
        global po
        po += message
        self.terminal.flush()  # 不启动缓冲,实时输出
        # self.log.flush()

    def flush(self):
        pass


# 用于生成结果截图
def imageGenerator():
    p = po.split("\n")
    biggest = 0
    for x in p:
        if len(x) > biggest:
            biggest = len(x)
    if biggest > 150:
        biggest = 150
    j = 30
    pygame.init()
    image = pygame.surface.Surface((biggest * 10, (len(p) + 2) * 20))
    image.fill("#282828")
    pygame.draw.rect(image, "#3c3f41", (0, 0, biggest * 12, 22))
    f = pygame.font.Font(".\\MSYHMONO.ttf", 13)
    image.blit(f.render(exe, True, "#c3c1c1", "#3c3f41"), (5, int((24 - f.get_height()) / 2)))
    pygame.draw.rect(image, "#747a80", (0, 20, len(exe) * 12, 3))
    for x in p:
        if "`!]" in x:
            x = x.replace("`!]", "")
            f.set_italic(True)
            image.blit(f.render(x, True, "#007f00", "#282828"), (15, j))
        else:
            f.set_italic(False)
            image.blit(f.render(x, True, "#c3c1c1", "#282828"), (15, j))
        j += 20
    pygame.image.save(image, "./temp.png")


# 用于截获input()输入的类
class LoggerInput(object):
    def __init__(self, stream=sys.stdin):
        self.inp = stream

    def readline(self):
        global args
        message1 = ""
        if args == "null":
            message1 = self.inp.readline()
        else:
            message1 = args
        global po
        po += "`!]" + message1 + "\n"
        return message1

    def flash(self):
        pass


# 用于处理配置文件
class Config:
    def __init__(self):
        self.c = open(".\\config", encoding="utf-8")
        self.s = self.c.read().split("\n")

    def getVar(self, key):
        flag = True
        for x in self.s:
            if key in x:
                flag = False
                return x.replace(key + "=", "").strip()


c = Config()
args = c.getVar("args")     # 这个变量用于自动传参，如果需要自动传入参数则在config改写这个变量，否则请填写null
name = c.getVar("name")     # 作者姓名
package = c.getVar("package") + "."     # 测试程序的包名
path = c.getVar("path")     # 需要测试的程序的所在路径，可填写相对路径
print("程序列表：")
py = os.listdir(path)
for i in py:
    if ".py" in str(i):
        print(str(i))
print("请输入需要测试的程序：")
exe = input().strip().replace(".py", "")
# 重定向输入输出流
sys.stdout = LoggerPrint(sys.stdout)
sys.stderr = LoggerPrint(sys.stderr)
sys.stdin = LoggerInput()
print()
startTime = datetime.datetime.now()
# 通过反射调用其他程序
try:
    __import__(package + exe)
except ModuleNotFoundError:
    print("该程序不存在！")
info(name)
imageGenerator()
