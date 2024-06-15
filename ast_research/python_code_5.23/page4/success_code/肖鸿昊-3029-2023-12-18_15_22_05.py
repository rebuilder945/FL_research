a=input().split(",")
b=eval(input())
c=[]
for i in range(len(a)):
    s=[]
    s.append(a[i])
    s.append(b[i])
    c.append(s)
print(c)
