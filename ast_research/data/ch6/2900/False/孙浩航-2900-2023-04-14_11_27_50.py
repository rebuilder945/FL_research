def sushu(n):
    for x in range(2,n//2+1):
        if n%x==0:
            return False
    return True
def huiwenshu(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
n=eval(input())
if n<2 or type(n)==float:
    print("illegal input")
else:
    for i in range(2,n):
        if sushu(i) and huiwenshu(i):
            print(i,end='')



