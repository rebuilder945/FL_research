a=list(input().split(','))
b=list(eval(input().split(',')))
c=[]
for i in range(len(a)):
    c.append([a[i],b[i]])
c.sort(key=b[i])
print(c)
