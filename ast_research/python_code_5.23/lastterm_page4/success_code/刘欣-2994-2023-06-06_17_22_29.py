lis=list(eval(input()))
n,m=input().split(',')
n=int(n)
m=int(m)
if n > len(lis)-1:
    print('error')
else:
    lis1=[lis[n]]*m
    newlis=lis+lis1
    print(newlis)
