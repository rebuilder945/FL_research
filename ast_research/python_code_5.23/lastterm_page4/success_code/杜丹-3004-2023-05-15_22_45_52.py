a=list(input().split())
m,n=map(int,input().split())
if m>len(a):
    print("error")
elif n>len(a):
    print("error")
else:
    a[m],a[n]=a[n],a[m]
print(a)


