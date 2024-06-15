a=input().split(",")
a=list(map(int,a))

b=list(range(a[0],(a[0]+a[2]*(a[1]-1)+1),a[2]))
print(b)

