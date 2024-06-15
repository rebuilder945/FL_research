def sushu(n):
    if n >= 2 and type(n) == int:
        for i in range(2,n//2+1):
            if n % i == 0:
                return False
        else:
            return True    
    else:
        return False
def huiwenshu(n):
    if str(n) == str(n)[ : :-1]:
        return True
    else:
        return False
n = eval(input())
if n < 2 and type(n) != int:
    print("illegal input")
for x in range(2,n+1):
    if sushu(x) and huiwenshu(x):
        print(x,end=' ')      
