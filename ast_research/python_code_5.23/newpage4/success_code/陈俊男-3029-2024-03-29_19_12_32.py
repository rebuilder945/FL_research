a=input().split(',')
b=eval(input())
lst=[]
for i in range(len(a)):
    c=[]
    c.append(a[i])
    c.append(b[i])
    lst.append(c)
print(lst)
