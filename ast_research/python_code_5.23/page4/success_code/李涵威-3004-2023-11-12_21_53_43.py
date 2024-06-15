def sushu(n):
    if n>=2 and type(n)==int:
        for i in range(2,n//2+1):
            if n%1==0:
                return False
            return True
    else:
        return False

a = eval(input())
lit = []
for i in a:
    if sushu(a):
        lit.append(a)
print(lit)
