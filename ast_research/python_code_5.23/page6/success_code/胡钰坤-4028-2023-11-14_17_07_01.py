def sushu(x):
    if x>=2 and type(x) == int:
        for i in range(2,x):
            if x % i == 0:
                return False
        return True
    else:
        return True
def huiwen(x):
    x = str(x)
    if x == x[::-1]:
        return True
    else:
        return False
n = eval(input())
if n<2 or type(n)!=type(1):
    print("illegal input")
else:
    for i in range(2,n):
        if sushu(n) and huiwen(n):
            print(n,end='')
