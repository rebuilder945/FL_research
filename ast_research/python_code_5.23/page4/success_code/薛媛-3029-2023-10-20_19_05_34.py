lst1=input().split(',')
lst1=list(lst1)
lst2=eval(input())
c=[]
for i in range(len(lst1)):
    d=[]
    d.append(lst1[i])
    d.append(lst2[i])
    c.append(d)
print(c)


