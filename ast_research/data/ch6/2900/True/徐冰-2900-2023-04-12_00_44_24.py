def huiwen(i):
    if str(i)==str(i)[::-1]:
        return True
    else:
        return False
def sushu(i):
    if i==2:
        return True
    else:
        for x in range(2,i//2+1):
            if i % x==0:
                return False
    return True
n=eval(input())
if n >1 and type(n)==int:
    ls=[x for x in range(2,n+1)]
    for i in ls:
        if huiwen(i) and sushu(i):
            print(i,end=" ")
else:
    print("illegal input")
