def sushu(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
def huiwensushu(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
n = eval(input())
if n <2 or type(n)!=int:
    print("illegal input")
else:
    for i in range(2,n):
        if sushu(i) and huiwensushu(i):
            print(i,end=' ')
                
        
    

