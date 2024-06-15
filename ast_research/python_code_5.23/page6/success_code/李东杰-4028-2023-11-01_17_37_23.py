a=eval(input())
def huiwenshu(x):
    a=str(x)
    if a==a[::-1]:
        return True
    else:
        return False
def sushu(x):
    for y in range(2,x):
        if x%y==0:
            return False
    return True
if type(a)==float or a<1 or a<0:
    print("illegal input")
else:
    for x in range(2,a):
        if huiwenshu(x) and sushu(x):
            print(x,end=" ")

