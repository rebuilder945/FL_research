a=eval(input())
n,m=eval(input())
if n<0:
    print("error")
elif m>len(a)-1:
    print("error")
else:
    del a[n:m]
    h=a
print(h)


