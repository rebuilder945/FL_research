a = eval(input())
def sushu(a):
    for i in range(2,a+1):
        if a % i == 0:
            return False
    return True
def huiwen(a):
    if str(a)[0] == str(a)[-1]:
        return True
    else:
        return False
if type(a) == type(1.1) or a<= 1:
    print('illegal input')
else:
    for x in range(2,a+1):
        if sushu(x):
            print(x,end = '')


