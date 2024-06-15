a=input()
b=a.split(" ")
n,m=(input().split(" "))
b[int(n)],b[int(m)]=b[int(m)],b[int(n)]
print(b)

