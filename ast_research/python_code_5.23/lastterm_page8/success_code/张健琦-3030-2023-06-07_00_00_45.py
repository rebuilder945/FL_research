a=input().split(',')
b=eval(input())
c=[]
d=[]
for i in range(len(b)):
    c=[a[i],b[i]]
    d.append(c)
    c=[]
d.sort(key=lambda x:x[-1])
print(d)

