a=input().split()
b=input().split()
c=b[0]
d=b[1]
if -len(a)<=int(c)<len(a):
    e=a[c]
    for i in range(int(d)):
        a.append(e)
    print(a)
else:
    print("error")
