a=input().split(",")
b=eval(input())
list1=[]
for x in range(len(a)):
    c=[]
    c.append(a[x])
    c.append(b[x])
    list1.append(c)
print(list1)
