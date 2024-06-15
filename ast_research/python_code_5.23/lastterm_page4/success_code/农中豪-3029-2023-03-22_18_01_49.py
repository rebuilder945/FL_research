a=input().split(',')
b=list(a)
c=eval(input())
d=()
e=[]
for i in range(len(c)):
    d=(b[i],c[i])
    e.append(list(d))
print(e)
print(d)
