import math
list=eval(input())
a=sum(list)/len(list)
b=math.modf(a)
if b[0]==0:
    print('%d'%a)
else:
    print('%.2f'%a)
