a=eval(input())
n,m=eval(input())
if m>len(a)-1:
    print("error")
else:
    for i in range(n,m):
        del a[i]
    print(a)    








