


a=eval(input())
n,m=eval(input())
if n<len(a) and m<len(a):
    a=a[0:n]+a[m:-1]+[a[len(a)-1]]
    print(a)
else:
    print("error")


