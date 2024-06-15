n=eval(input())
num=[]
while n>=1:
    a=(n+5)%10
    num.append(a)
    n=n//10
print(*num,sep='')
