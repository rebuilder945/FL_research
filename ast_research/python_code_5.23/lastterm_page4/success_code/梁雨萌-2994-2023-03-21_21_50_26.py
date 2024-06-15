a=list(map(int,input().split(",")))
b,c=eval(input())
if abs(b)<len(a):
    rep=a[b]
    for i in range(1,c+1):
        a.append(rep)
        print(a)
else:
    print("error")
