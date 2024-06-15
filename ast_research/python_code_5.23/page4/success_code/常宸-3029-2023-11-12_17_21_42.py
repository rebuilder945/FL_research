a= input().split(",")
b=eval(input())
c=[]
for i in range(len(a)):
    temp=[]
    temp.append(a[i])
    temp.append(b[i])
    c.append(temp)
print(c)
