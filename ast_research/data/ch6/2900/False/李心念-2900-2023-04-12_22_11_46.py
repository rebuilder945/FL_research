def sushu(n):
    for x in range(2,n//2):
        if n%x==0:
            return False
    return True
def huiwen(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
a = eval(input())
if a<2 or type(a) != int:
    print("illegal input")
else:
    for x in range(2,a):
        if sushu(x) and huiwen(x):
            print(x,end=' ')
