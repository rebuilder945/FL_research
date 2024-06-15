def sushu(n):
    if n >= 2 and type(n) == int:
        for i in range(2,n//2+1):
            if n % 1==0:
                return True
    else:
        return False
def huiwensushu(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
n=eval(input())
if n<2 or type(n)!=type(1):
    print("illegal input")
else:
    for i in range(2,n):
        if sushu(i) and huiwensushu(i):
            print(i,end=" ") 
