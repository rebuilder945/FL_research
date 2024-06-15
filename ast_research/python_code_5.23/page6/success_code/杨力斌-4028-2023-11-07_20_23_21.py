def sushu(n):
    if n >= 2 and type(n) == int:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    else:
        return False

def huiwensu(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
n = eval(input())
if n < 2 or type(n) != int:
    print("illegal input")
else:
    for i in range(2,n):
        if sushu(i) and huiwensu(i):
            print(i,end=" ")
