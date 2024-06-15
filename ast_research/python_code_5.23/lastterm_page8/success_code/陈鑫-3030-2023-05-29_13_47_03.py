a=input().split(',')
b=eval(input()).split(',')
c=[[0 for i in range(2)]for x in range(len(a))]
for i in range(len(a)):
    c[i][0]=a[i]
    c[i][1]=b[i]
c.sort(key=lambda x:x[1])
print(c)
