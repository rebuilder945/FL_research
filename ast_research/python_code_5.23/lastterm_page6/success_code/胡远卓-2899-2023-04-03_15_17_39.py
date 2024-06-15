def check(x,n,m):
    a,b,c=x%10,(x//10)%10,x//100
    if a==b or b==c or a==c:
        return False
    if n>a or a>=m:
        return False
    if n>b or b>=m:
        return False
    if n>c or c>=m:
        return False
    return True

n,m=input().split(" ")
n=eval(n)
m=eval(m)
res=""
for x in range(100,1000):
    if check(x,n,m):
        res+=str(x)+' '
print(res[:-1])
