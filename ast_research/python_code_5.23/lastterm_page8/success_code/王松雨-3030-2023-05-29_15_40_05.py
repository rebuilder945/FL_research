a=list(eval(input().split(",")))
b=list(map(int,input().split(",")))
c=[]
for i in range(len(a)):
    c.append([a[i],b[i]])
    print(c)

