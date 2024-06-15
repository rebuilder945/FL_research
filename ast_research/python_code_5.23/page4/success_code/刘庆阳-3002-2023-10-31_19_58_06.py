import math
def a(y):
    print("%.2f" %(sum(y)/len(y)))
b=eval(input())
b =math.modf(a)
if b[0]==0:
	print('%d'%a)
else:
	print('%.2f'%a)
a(b)
