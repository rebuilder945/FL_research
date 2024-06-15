a = input().split(',')
b = list(map(int,input().split(',')))
n = [[a[x],b[x]]for x in range(len(a))]
n.sort(key=lambda x:x[1])
print(n)
