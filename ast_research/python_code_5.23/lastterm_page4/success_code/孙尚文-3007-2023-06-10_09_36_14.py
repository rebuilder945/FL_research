a=eval(input())
b,c=eval(input())
if b<=c and 0<=b<=len(a) and 0<=c<=len(a):
    d=a[0:b]+a[c:]
    print(d)
else:
    print("error")

