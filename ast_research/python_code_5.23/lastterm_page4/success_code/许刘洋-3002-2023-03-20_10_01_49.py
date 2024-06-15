import math
lst=eval(input())
a=sum(lst)/len(lst)
b=math.modf(a)    #取小数和整数，小数为b[0],整数为b[1]
if b[0]==0:
    print("%d"%a)    #若无‘%d’进行整数输出，直接print(a)输出则会带有一位小数点
else:
    print("%.2f"%a)

