from re import A


a=eval(input())
n,m=eval(input())
if n<0:
    print("error")
elif m>len(a)-1:
    print("error")
else:
    a.remove(n,m)
    h=a
print(h)


