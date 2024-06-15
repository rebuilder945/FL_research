a=input()
a=a.split(",")
n,m=eval(input())
b=len(a)
if n>b-1:
    print("error")
else:
    c=a[n]
    del a[n]
    for i in range(m**2):
        a.append(c)
    print(a)

