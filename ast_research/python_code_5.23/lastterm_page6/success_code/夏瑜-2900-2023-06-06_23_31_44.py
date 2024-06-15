def sushu(n):
    if n>=2:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
def huiwen(n):
    if str(n)==str(n)[::-1]:
        return  True
    else:
        return  False
    
n=eval(input())
if n<2 or type(n)!=type(1):
    print("illegal input")
else:
    for i in range(2,n):
        if sushu(i) and huiwen(i):
            print(i,end=' ')

    



