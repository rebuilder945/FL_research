a=input().split(",")
b=eval(input())
c=[]
for i in range(len(a)):
    s=[]
    s.append(a[i-1])
    s.append(b[i-1])
    c.append(s)
print(c)
