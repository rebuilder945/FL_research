a=eval(input())
b=[]
for i in range(0,len(a)):
    if a[i]==0:
        b.append(a[i])
while 0 in a:
    a.remove(0)
c=[]
c=a+b
print(c)
