import math
ls=eval(input())
a=sum(ls)/len(ls)
b=math.modf(a)
if b[0]==0:
    print('%d'%(a))
else:
    print('%.2f'%(a))
# if type(a)=='float':
#     print('%2f.d'%(a))
# else:
#     print(int(a))

