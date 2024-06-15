a=list(map(int,input().split(',')))
n,m=eval(input())
b=[]
if n <len(a) and n>=0:
    d=a[n]
    for i in range(m):
        b.append(d)
    del a[n]    
    print(a+b)
else:
    print("error")        


