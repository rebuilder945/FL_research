def huiwen(x:int):
    temp = str(x)
    if temp == temp[::-1]:
        return True
    return False

def sushu(x:int):
    if x == 2:
        return True
    elif x == 1:
        return False
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

n=eval(input())
if n==int and n>0:
    for n in range(1,n+1):
        if huiwen(n) and sushu(n)==True:
            print(n,end=" ")
elif n!=int or n<=0:
     print("illegal input")



