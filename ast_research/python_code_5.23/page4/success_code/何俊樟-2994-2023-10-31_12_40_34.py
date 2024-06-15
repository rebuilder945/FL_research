a=input().split(",")
b,c=eval(input())
d=len(a)-1
if c>d:
    print("error")
else:
    e=[a[b]]
    e=e*c
    a.extend(e)
    print(a)
