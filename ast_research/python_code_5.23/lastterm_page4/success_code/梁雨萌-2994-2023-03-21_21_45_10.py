a=list(map(int,input().split(",")))
b,c=eval(input())
if abs(b)>=len(a):
    print("error")
else:
    rep=a[b]
    for i in range(1,c+1):
        a.append(rep)
print(a)
