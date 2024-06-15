a=list(map(int,input().split(',')))
n,m=eval(input())
if -len(a)<n<len(a)-1 :
    b=a[n]
    for i in range(m):
        a.append(b)
    print(a)
else:
    print("error")
