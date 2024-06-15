def sushu(n):
    for x in range(2,n//2):
        if n%x==0:
            return False
        else:
            return True
def huiwen(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
a = eval(input())
if a<=0 or type(a)==float:
    print("illegal input")
else:
    for x in range(1,a):
        if sushu(a) and huiwen(a):
            print(x,end=' ')
