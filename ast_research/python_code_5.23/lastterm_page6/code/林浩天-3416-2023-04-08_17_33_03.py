#输入100c      输出212.00F

 # 输入不符合格式要求，输出“Error”     

TempStr = input()

if TempStr[-1] in [‘F’,‘f’]:

C = (eval(TempStr[0:-1]) - 32)/1.8

print("%.2fC"%(C))
elif TempStr[-1] in [‘C’,‘c’]:

F = 1.8*eval(TempStr[0:-1]) + 32

print("%.2fF"%(F))
else:

print("Error")
#————————————————
#版权声明：本文为CSDN博主「谭你一个脑瓜崩」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/qq_54226199/article/details/127326303
