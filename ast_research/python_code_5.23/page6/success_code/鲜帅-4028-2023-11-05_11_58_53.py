def sushu(x):
    if x>2 and type(x)==int:
        for i in range(2,int(x**(1/2))+1):
            if x%i==0:
                return False
        return True
    else:
        return False
def huiwenshu(x):
    if str(x)==str(x)[::-1]:
        return True
    else:
        return False
n = eval(input())
if n<0 or type(n)==float:
    print('illegal input')
else:
    for i in range(2,n):
        if sushu(i) and huiwenshu(i):
            print(i,end=' ')
