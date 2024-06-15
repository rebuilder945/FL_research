a=[]
a.extend(input().split())
b,c=eval(input())
if abs(b)>=len(a):
    print("error")
else:
    rep=a[b]
    del a[b]
    for i in range(1,c+1):
        a.append(b)
print(a)
