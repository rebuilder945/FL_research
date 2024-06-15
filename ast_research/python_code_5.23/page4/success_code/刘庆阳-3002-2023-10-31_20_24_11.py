import math
def a(y):
    b = sum(y)/len(y)
    c = math.floor(b)
    if b - c!= 0:
        print("%.2f" %(b))
    else:
        print("%d" %(b))
    return b    
sums=eval(input())
a(sums)
