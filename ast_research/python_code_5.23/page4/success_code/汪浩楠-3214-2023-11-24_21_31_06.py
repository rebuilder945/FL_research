lst=eval(input())
a=lst.count(0)
b=[]
for i in lst:
    if i !=0:
        b.append(i)
for i in range(a):
    b.append(0)
print(b)


