# 素数的函数
def sushu(n):
    if n >= 2 and type(n) == int:
        for i in range(2,n//2+1):
            if n % i == 0:
                return False
        return True
    else:
        return False

# 回文数的函数
def huiwenshu(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
list0 = []
n = eval(input())
if n <= 0 or type(n) != type(1):
    print("illegal input")
else:
    for i in range(n):
        if sushu(i) and huiwenshu(i) == True:
            list0.append(i)
    for i in range(len(list0)):
        print(list0[i],end=" ")
