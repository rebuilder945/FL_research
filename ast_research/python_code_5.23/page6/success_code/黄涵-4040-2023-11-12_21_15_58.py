#以下是一段温度转换程序，可以实现华氏温度和摄氏温度的转换，
#请自行阅读程序，在理解程序的基础上，仿照此程序，写一个人民币和美元之间的货币转换程序。
a = input()
if a[0] == "$" :
    b = (eval(a[1:]))*6.78
    print("&%.2f"%b)
elif a[0] == "&" :
    b = (eval(a[1:]))/6.78
    print("$%.2f"%b)
elif a[0:3] == "USD" :
    b = (eval(a[3:]))*6.78
    print("RMB%.2f"%b)
elif a[0:3] == "RMB" :
    b = (eval(a[3:]))/6.78
    print("USD%.2f"%b)
else :
    print("Error")
