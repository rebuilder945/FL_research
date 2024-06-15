import math
a=eval(input())
s=0
for x in a:
    s+=x
b=s/len(a)
if b>math.floor(b):
    print("%.2f"%b)
elif b==math.floor(b):
    print("%.d"%b)
