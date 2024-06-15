
import math
list=eval(input())
ave=sum(list)/len(list)
b=math.modf(ave)
if b[0]==0:
    print('%d'%(ave))
else:
    print('%.2f'%(ave))

