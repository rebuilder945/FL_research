import math
def zhishu(m):
    if m <=1:
        return False
    for i in range(2,int(math.sqrt(m)+1)):
        if m%i==0:
            return False
    return True
def huiwenshu(m):
    sm=str(m)
    sm1=""
    for y in sm:
        sm1=y+sm1
    if sm1==sm:
        return True
n=eval(input())
if math.floor(n)==n and n >0:
    for m in range(n):
        if huiwenshu(m):
            if zhishu(m):
                print(m,end=" ")
else:
    print("illegal input")
