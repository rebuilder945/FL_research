a=list(input().split())
n,m=eval(input().split())
if n>len(a):
    print("error")
elif m>len(a):
    print("error")
else:
    a[n]=a[m]
print(a)
