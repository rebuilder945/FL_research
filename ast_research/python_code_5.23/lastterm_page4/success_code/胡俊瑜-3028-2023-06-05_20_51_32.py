n,m,l=eval(input())
midlelist=[x for x in range(n,n+m*l+1)]
result=midlelist[0:n+m*l:l]
print(result)

