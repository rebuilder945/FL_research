a=input()
b=a.split()
n, m = map(int, input().split())
b[n],b[m]=b[m],b[n]
print(b)


