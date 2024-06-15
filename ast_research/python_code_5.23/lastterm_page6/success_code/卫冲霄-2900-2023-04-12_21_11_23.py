def huiwenshu(m):
    if str(m)==str(m)[::-1]:
        return True
    else:
        return False
import math
def sushu(m):
    if m>=2 and type(m)==int:
        for i in range(2,int(math.sqrt(m))+1):
            if m%i==0:
                return False
        return True
    else:
        return False
ls=[]
n=int(input())
if type(n)!=int or n<0:
    print("illegal input")
else:
    for i in range(n):
        if huiwenshu(i) and sushu(i):
            ls.append(i)
    print(*ls,end="")


