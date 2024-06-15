a = input()
if a[0]=="$":                               #字符串的切片————字符串第一个字符是$
    RMB=eval(a[1:-1]+a[-1])*6.78            #字符串的切片————[1:-1]:第二位到倒数第二位;[-1]:字符串的最后一位；字符串的加法
    print("&{:.2f}".format(RMB))            #format格式化输出————{:.2f}表示以两位浮点数输出
elif a[0:3]=="USD":                         #字符串的切片————字符串前三个字符分别为USD
    RMB=eval(a[3:-1]+a[-1])*6.78
    print("RMB{:.2f}".format(RMB))
elif a[0]=="&":                             #elif的用法，在if和else之间插入更多判断分类
    USD=eval(a[1:-1]+a[-1])/6.78
    print("${:.2f}".format(USD))
elif a[0:3]=="RMB":
    USD=eval(a[3:-1]+a[-1])/6.78
    print("USD{:.2f}".format(USD))
else:
    print("Error")
