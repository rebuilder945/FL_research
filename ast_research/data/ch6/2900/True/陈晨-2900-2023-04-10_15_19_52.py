import math

def sushu(x):
    if x<2:
        return False

    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False

    return True

def huiwenshu(x):
    if x < 0 or (x % 10 == 0 and x != 0):
       return False
    elif not x // 10:
       return True
    else:
        hou = 0
        while (x > hou):
          hou = hou * 10 + x % 10
          x //= 10
    if x == hou or x == (hou // 10):
         return True
    else:
         return False

n=eval(input())
daan=[]
if n>=1 and n%1==0:
    for x in range(n+1):
        if huiwenshu(x) and sushu(x):
            daan.append(x)
        else:
            pass
    print(" ".join(str(i) for i in daan))
else:
    print("illegal input")



