n=eval(input())
x=range(1,n+1)
li=list(x)
for i in range(n-1):
    li[i]=li[i+1]
li[n-1]=1
print(li)
