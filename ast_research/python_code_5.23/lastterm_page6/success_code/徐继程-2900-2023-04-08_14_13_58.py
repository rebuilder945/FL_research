def sushu(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
a=0
m=eval(input())
if m<=0 or type(m)!=type(0):
    print('illegal input')
else:
    for i in range(2,m):
        n=str(i)
        if n[::-1]==n and sushu(i):
            print(i,end=' ')
            a+=1
    if a==0:
        print('illegal input')


