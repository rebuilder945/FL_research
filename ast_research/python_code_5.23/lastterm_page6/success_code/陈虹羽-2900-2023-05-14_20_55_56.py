def sushu(n):
    if n<2 or type(n)!=int:
        return False
    else:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        return True
def huiwen(n):
    n=str(n)
    if n==n[::-1]:
        return True
    else:
        return False

n=eval(input())
b=[]
if type(n)!=int or n<=0:
    print('illegal input')
else:
    for i in range(n):
        if sushu(i) and huiwen(i):
            b.append(i)
        
    print(' '.join(str(e) for e in b))




