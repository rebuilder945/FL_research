a=input()
b=a.split(" ")
n,m=input().split(" ")
b[n]=b[m],b[m]=b[n]
print(b)
