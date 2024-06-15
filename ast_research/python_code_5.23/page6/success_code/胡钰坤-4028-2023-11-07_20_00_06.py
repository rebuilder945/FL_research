def sushu(x):
    if x>=2:
        for i in range(2,x):
            if x % i == 0:
                return True
    else:
        return False

def huiw(x):
    a = str(x)
    for i in a:
        if a[::-1] == a:
            return True
        else:
            return False

n = eval(input())
if n<2 or type(n)!=type(1):
    print("illegal input")
else:
    for i in range(2,n):
        if sushu(i) and huiw(i):
            print(i,end=' ')
