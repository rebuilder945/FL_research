def f1(x):
    return 6*x**2+1
def f2(x):
    return (3*x-60)**0.5
def f3(x):
    return 100/(x+1)
n=float(input())
if n<20:
    print('%.2f'%f1(n))
elif n>=20 and n<40:
    print('%.2f'%f2(n))
else:
    print('%.2f'%f3(n))

#————————————————
#版权声明：本文为CSDN博主「谭你一个脑瓜崩」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/qq_54226199/article/details/127326303
