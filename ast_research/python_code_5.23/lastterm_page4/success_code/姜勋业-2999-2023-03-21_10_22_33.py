a=input().split(" ")
m,n=eval(input().split(" "))
i=a[m]
j=a[n]
a[m]=j
a[n]=i
print(a)
