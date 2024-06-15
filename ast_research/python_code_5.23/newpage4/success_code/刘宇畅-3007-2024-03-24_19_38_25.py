a=eval(input())
n,m=eval(input())
y=len(a)
while n<y and m<y:
    for x in a[n:m]:
        del a[a.index(x)]
    print(a)
    break
else:
    print("error")
    

