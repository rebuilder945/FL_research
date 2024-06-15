a=eval(input())
n,m=eval(input())
b=len(a)
if n>b or m>b:
    print("error")
else:
    for i in a[n:m]:
        a.remove(i)
    print(a)
