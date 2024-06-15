def sushu(n):
    if n > 1 and type(n) == int:
        for i in range(2,n//2 + 1):
            if n % i == 0:
                return False
        return True         #for或while循环的else子句有时候可以省略 和for对齐
    else:
        return False
def huiwenshu(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
n = eval(input())
if n <= 1 or type(n) != type(1):
    print("illegal input")
else:                    
    for i in range(2,n+1):
        if sushu(i) and huiwenshu(i):
            print(i,end=" ")

