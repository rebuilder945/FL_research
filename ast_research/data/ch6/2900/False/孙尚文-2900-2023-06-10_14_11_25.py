def huiwenshu(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
def sushu(n):
    if n>=2 and type(n)==int:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        return True
    else:
        return False
a=eval(input())
if a>0 and type(a)==int:
    for i in range(a):
        if huiwenshu(a) and sushu(a):
            print(a,end=" ")
else:
    print("illegal input")
