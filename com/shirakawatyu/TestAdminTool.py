import datetime
import os
import sys
import time
from io import BytesIO

import PIL.Image
import pygame
import win32clipboard

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
        "%Y-%m-%d %H:%M:%S") + "\n执行耗时：" + str(int((
                                                               datetime.datetime.now() - startTime).total_seconds() * 1000)) + "ms" + "\n程序作者：" + name1 + "\n测试台作者：ShirakawaTyu(方律奔)" + "\n测试台版本：1.2"


# 用于截获print()输出的类
class LoggerPrint(object):
    def __init__(self, stream=sys.stdout):
        self.terminal = stream

    def write(self, message):
        self.terminal.write(message)
        global po
        po += message
        self.terminal.flush()

    def flush(self):
        pass


# 用于生成结果截图
def imageGenerator(margin, font):
    p = po.split("\n")
    biggest = 0
    b = ""
    pygame.init()
    f = pygame.font.Font(".\\" + font, 13)
    for x in p:
        if f.size(x)[0] > biggest:
            biggest = f.size(x)[0]
            b = x
    # if biggest > 150:
    #     biggest = 150
    # print(b)
    j = 30
    image = pygame.surface.Surface((biggest + margin * 2, (len(p) + 2) * 20))
    image.fill("#282828")
    pygame.draw.rect(image, "#3c3f41", (0, 0, biggest + margin * 2, 22))
    image.blit(f.render(exe, True, "#c3c1c1", "#3c3f41"), (5, int((24 - f.get_height()) / 2)))
    pygame.draw.rect(image, "#747a80", (0, 20, len(exe) * 12, 3))
    for x in p:
        if x.find("`!]") == 0:
            x = x.replace("`!]", "")
            f.set_italic(True)
            image.blit(f.render(x, True, "#007f00", "#282828"), (15, j))
        elif x.find("`!]") > 0:
            x = x.split("`!]")
            f.set_italic(False)
            image.blit(f.render(x[0], True, "#c3c1c1", "#282828"), (15, j))
            f.set_italic(True)
            image.blit(f.render(x[1], True, "#007f00", "#282828"), (15 + len(x[0]) * 13, j))
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
        global po
        if args == "null":
            message1 = self.inp.readline()
            po += "`!]" + message1
        else:
            message1 = args
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
        if flag:
            return None


# 将图片放入剪贴板
def imageToClip(filepath):
    img = PIL.Image.open(filepath)
    out = BytesIO()
    img.save(out, "BMP")
    data = out.getvalue()[14:]
    out.close()
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()
    print("\n提示：运行结果图已拷贝至剪贴板")


c = Config()
args = c.getVar("args")  # 这个变量用于自动传参，如果需要自动传入参数则在config改写这个变量，否则请填写null
name = c.getVar("name")  # 作者姓名
package = c.getVar("package") + "."  # 测试程序的包名
path = c.getVar("path")  # 需要测试的程序的所在路径，可填写相对路径
m = int(c.getVar("margin"))  # 文字边距
f = c.getVar("font")
print("程序列表：")
py = os.listdir(path)
for i in py:
    if ".py" in str(i):
        print(str(i))
print("请输入需要测试的程序：")
exe = input().strip().replace(".py", "")
# 重定向输入输出流
sys.stdout = LoggerPrint()
sys.stderr = LoggerPrint()
sys.stdin = LoggerInput()
print()
startTime = datetime.datetime.now()
# 通过反射调用其他程序
try:
    __import__(package + exe)
except ModuleNotFoundError:
    print("该程序不存在！")
info(name)
imageGenerator(m, f)
imageToClip(".\\temp.png")
