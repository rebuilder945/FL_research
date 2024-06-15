a=input().split(',')
b=input().split(',')
c=[]
for x in range(len(a)):
    c.append([a[x],eval(b[x])])
print(c)
