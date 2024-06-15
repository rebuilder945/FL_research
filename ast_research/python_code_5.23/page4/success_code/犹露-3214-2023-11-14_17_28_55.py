a = eval(input())
c=[]
for i in range(len(a)):
    if a[i]!=0:
        c.append(a[i])
d =[x for x in a if x not in c]
m= c+d
print(m)
