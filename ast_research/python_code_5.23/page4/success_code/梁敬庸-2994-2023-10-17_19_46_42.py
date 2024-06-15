a=list(map(int,input().split(',')))
n,m=eval(input())
b=[]
if n <len(a) and n>=0:
    for i in range(m):
        b.append(a[n])
    print(a+b)
else:
    print("error")        


