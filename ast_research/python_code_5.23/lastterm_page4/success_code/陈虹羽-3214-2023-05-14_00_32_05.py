a=eval(input())
b=0
for i in a:
    if i==0:
        b+=1
if b!=0:
    for i in range(b):
        a.remove(0)
    for i in range(b):
        a.append(0)
    print(a)
else:
    print(a)
