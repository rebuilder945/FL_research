import turtle


def huiwen(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
def sushu(n):
    for i in range (2,n):
        if n%i==0:
            return False
    return True
n=eval(input())
if n<2 or n!=int(n):
    print("illegal input")
else:
    for i in range(2,n):
        if huiwen(i) and sushu(i):
            print(i,end=' ')

