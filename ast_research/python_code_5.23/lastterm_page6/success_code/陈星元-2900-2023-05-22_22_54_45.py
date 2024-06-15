from math import*
def huiwen(a):
    if str(a)==str(a)[::-1]:
        return True
    else:
        return False
def sushu(num):
    if num<2:
        return False
    elif num==2:
        return True
    else:
        for x in range(2,int(sqrt(num))):
            if num%x==0:
                return False
        return True
n=eval(input())
if n<0 or type(n)==type(1.5):
    print("illegal input")
else:
    for x in range(2,n+1):
        if huiwen(x) and sushu(x):
            print(x,end=" ")
        else:
            continue


