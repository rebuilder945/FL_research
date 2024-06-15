from turtle import Turtle


def issushu(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
def huiwensushu(number):
    for i in range(number):
        if str(i)==str(i)[::-1]and issushu(i):
            print(i,end=' ')
n=input()
if n.isdigit() and int(n)>1:
    huiwensushu(int(n))
else:
    print('illegal input')
