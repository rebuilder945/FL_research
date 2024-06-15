lst=eval(input())
a=[]
b=[]
for i in lst:
    if (i==0):
        b.append(0)
    else:
        a.append(i)
print(a+b)
