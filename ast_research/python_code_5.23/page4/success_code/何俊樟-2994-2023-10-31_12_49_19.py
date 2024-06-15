a=input().split(",")
for x in range(len(a)):
    a[x]=int(a[x])
b,c=eval(input())
d=len(a)-1
if b>d or -b>d+1:
    print("error")
else:
    e=[a[b]]
    e=e*c
    a.extend(e)
    print(a)
