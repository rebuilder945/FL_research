a = input()
b = a.split()
n,m = list(map(int,input().strip().split()))
b[n],b[m] = b[m],b[n]
print(b)
