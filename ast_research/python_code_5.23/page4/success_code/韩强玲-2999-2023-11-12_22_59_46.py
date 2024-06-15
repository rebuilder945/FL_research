a = input().split(" ")
m,n = map(int,input().split(" "))
a[m],a[n]=a[n],a[m]
print(list(a))

