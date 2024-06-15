n,m,l = map(int,input().split(','))
r = [n + l*i for i in range(m)]
print(r)
