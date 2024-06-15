def sushu(n):
    if n > 1:
        for i in range(2,n//2+1):
            if n % i== 0:
                return False
    return True

def huiwenshu(n):
    a=str(n)
    if a[::-1]==a:
        return True
    else:
        return False
    
n = eval(input())
if n<2 or type(n)!=type(1):
    print('illegal input')
else:
    for i in range(2,n):
        if sushu(i) and huiwenshu(i):
            print(i,end=' ')

