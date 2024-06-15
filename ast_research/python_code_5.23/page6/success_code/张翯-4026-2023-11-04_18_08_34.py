n=eval(input())
lst=[]
a,b=2,1
for x in range(n):
    c=a/b
    lst.append(c)
    a+=b
    b=a-b
d=sum(lst)
print("%.4f"%d)


