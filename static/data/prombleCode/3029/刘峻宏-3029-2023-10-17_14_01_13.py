a=list(input().split(','))
b=eval(input())
i=0
c=[]

for i in range(len(b)):
    c.append([a[i],b[i]])
    i+=1
print(c)
