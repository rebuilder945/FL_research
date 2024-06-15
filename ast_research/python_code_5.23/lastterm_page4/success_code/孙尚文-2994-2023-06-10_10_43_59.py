a=[1,2,3,4,5]
b=[2,3]
c=b[0]
d=b[1]
if -len(a)<=int(c)<len(a):
    e=a[c]
    for i in range(int(d)):
        a.append(e)
    print(a)
else:
    print("error")
