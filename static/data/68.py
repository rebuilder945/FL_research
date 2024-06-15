a = eval(input())
av = 0
c = 0
for x in a:
    c = c + x
    av = av + 1
ave = c / av
print("%.2f" % ave)  # 使用了错误的格式化字符串方式,使用 %.2f 来表示输出浮点数 ave，并保留两位小数。