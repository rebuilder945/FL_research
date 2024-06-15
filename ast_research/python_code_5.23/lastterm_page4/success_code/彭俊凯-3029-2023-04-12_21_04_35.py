a=list(input().split(','))
b=eval(input())
print([[a[i]]+[b[i]]for i in range(len(a))])
