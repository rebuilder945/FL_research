a=eval(input())
n,m=eval(input())
c=[]
if n<len(a) or n>=len(a):
    print("error")
else:
    c.append(a[n]*m)
a.append(c)
print(a)
