a=list(input().split(','))
b=eval(input())
n=len(b)
c=[[a[i],b[i]] for i in range(0,n)]
print(c)
