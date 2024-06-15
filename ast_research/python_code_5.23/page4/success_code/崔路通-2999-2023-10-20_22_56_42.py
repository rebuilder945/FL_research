a=list(input().split(" "))
A=input().split(" ")
n=int(A[0])
m=int(A[1])
b=a.copy()
a[n]=b[m]
a[m]=b[n]
print(a)

