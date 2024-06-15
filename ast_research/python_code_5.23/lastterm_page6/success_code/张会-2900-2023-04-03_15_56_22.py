def sushu(n):
    if n > 1:
        for i in range(2,n):
            if n % i== 0:
                return n
    return 1
def huiwenshu(n):
    a=str(n)
    if a[::-1]==a:
        return n
n = eval(input())
