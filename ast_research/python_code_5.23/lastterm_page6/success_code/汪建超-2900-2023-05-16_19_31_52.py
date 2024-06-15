def huiwen(x):
    x = str(x)
    if x ==x [::-1]:
        return True 
    else:
        return False
def sushu(x):
    for i in range(2,x):
        if x%i == 0:
            return False
        else:
            return True
lst = []
n = int(input())
if n <0 or type(n)==float:
    print("illegal input")
else:
     for i in range(2,n):
        if huiwen(i)and sushu(i):
            lst.append(i)
print(*lst)
