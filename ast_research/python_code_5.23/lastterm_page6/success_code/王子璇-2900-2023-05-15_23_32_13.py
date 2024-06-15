def sushu(a):
    if a<=1:
        return False
    for i in range(2,a):
        if a%i==0:
            return False
    return True
def huiwenshu(a):
    a=str(a)
    b=a[::-1]
    if a==b:
        return True
    return False
n=eval(input())
if int(n)==n and n>0:
    for i in range(n):
        if sushu(i) and huiwenshu(i):
            print(i,end="")
else:
    print('illegal input')
