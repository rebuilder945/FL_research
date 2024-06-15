a=list(input())

b=[]
for i in range(len(a)):
    a[i]=int(a[i])
    a[i]=(a[i]+5)%10
    
    b.append(a[i])
b[0],b[-1]=b[-1],b[0]
b[1],b[-2]=b[-2],b[1]
for x in b:
    print(x,end='')
