str1 = ""
while str1 != "exit()":
    str1 = input("请输入您想要统计的字符串，如果要退出，请输入 exit()").lower()
    eng = 0
    num = 0
    space = 0
    other = 0
    for i in str1:
        if str1 != "exit()":
            if 'A' <= i <= 'z':
                eng += 1
            elif '0' <= i <= '9':
                num += 1
            elif i == ' ':
                space += 1
            else:
                other += 1
    if str1 != "exit()":
        print("字母：" + str(eng) + "数字：" + str(num) + "空格：" + str(space) + "其他：" + str(other))
