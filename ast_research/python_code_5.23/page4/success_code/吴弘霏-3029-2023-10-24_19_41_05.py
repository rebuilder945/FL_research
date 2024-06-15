a=input()
b=eval(input())
c=[]
a=a.split(",")
for i in range(len(a)):
    d=[a[i],b[i]]
    c.append(d)
print(c)
