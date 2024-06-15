a=eval(input())
b=a.count(0)
c=b*[0]
lis=[]
for i in a:
    if i!=0:
        lis.append(i)
d=lis+c
print(d)
