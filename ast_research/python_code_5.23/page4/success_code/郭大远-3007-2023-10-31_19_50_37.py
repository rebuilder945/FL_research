a=eval(input())
n,m=eval(input())
if n<0:
    print("error")
elif n>=m:
    print("error")
else:
    del a[n:m]
    h=a
print(h)





