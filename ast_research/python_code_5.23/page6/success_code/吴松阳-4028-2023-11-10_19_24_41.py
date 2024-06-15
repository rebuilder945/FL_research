a = eval(input())
def sushu(a):
    for i in range(2,a+1):
        if a % i == 0:
            return False
    return True
def huiwen(a):
    p = a
    k = 0
    while p != 0:
        k = k*10 +p%10
        p = p//10
    if k == a:
        return True
    else:
        return False
if type(a) == type(1.1) or a<= 1:
    print('illegal input')

for x in range(2,a+1):
    if huiwen(x) and sushu(x):
        print(x)


