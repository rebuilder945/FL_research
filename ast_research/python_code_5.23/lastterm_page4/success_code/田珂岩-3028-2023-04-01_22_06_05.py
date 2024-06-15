#n, m, l = list(map(int,input().split(',')))
n, m, l = eval(input())
ls = [x for x in range(n,n+m*l,l)]
print(ls)
