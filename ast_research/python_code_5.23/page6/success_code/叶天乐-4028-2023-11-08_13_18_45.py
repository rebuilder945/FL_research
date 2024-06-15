n = eval(input())
def sushu(n):
    if n>=2 and type(n)==int:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        return True
    else:
        return False
def huiwenshu(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
if n<2 or type(n)!=int:
    print("illegal input")
else:
    for i in range(2,n):
        if sushu(i) and huiwenshu(i):
            print(i,end=' ')

