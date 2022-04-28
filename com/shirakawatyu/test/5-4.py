a = ["", "一", "二", "三", "四", "五", "六", "七", "八", "九"]
for i in range(1, 10):
    for j in range(1, i + 1):
        multi = (str(j) + str(i)).replace(str(i), a[i]).replace(str(j), a[j])
        if i * j < 10:
            multi = multi + "得" + a[i * j]
        elif i * j == 10:
            multi = multi + "一十"
        elif i * j < 20:
            multi = multi + "十" + a[(i * j) % 10]
        elif (i * j % 10) == 0:
            multi = multi + a[int((i * j) / 10)] + "十"
        else:
            multi = multi + a[int((i * j) / 10)] + "十" + a[(i * j) % 10]
        print(multi, end=" \t")
    print()
