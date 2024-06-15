def sushu(n):
    for i in range(2,n//2+1): #判断素数的条件，到其一半加一即可，也可range(2,n)
        if n%i == 0:
            return False
    return True
def huiwen(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
n = eval(input())
if n<2 or type(n) != type(1):
    print("illegal input")
else:
    for i in range(2,n):
        if sushu(i) and huiwen(i):
            print(i,end = ' ')
