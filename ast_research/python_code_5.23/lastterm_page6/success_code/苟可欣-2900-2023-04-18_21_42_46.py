def sushu(n):
    for i in range(2,n//2+1):
        if n % i ==0:
            return False
    return True
def huiwen(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
n=eval(input())
if n < 2 or type(n) != int:
    print("illgal input")
else:
    for i in range(2,n):
        if sushu(i) and huiwen(i):
            print(i,end=' ')
