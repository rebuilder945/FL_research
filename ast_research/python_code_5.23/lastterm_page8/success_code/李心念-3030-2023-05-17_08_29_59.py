a = input().split(',')
b = list(map(int,input().split(',')))
n = [[a[x],b[x]]for x in range(len(a))].sort(key=lambda x:x[1])
print(n)
