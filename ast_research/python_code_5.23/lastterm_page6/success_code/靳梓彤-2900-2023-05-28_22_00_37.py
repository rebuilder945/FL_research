import math
def zs(m):
    if m<=1:
        return False
    for i in range(2,int(math.sqrt(m)+1)):
        if m%1==0:
            return False
    return True
def hws(m):
    sm=str(m)
    sm1=""
    for y in sm:
        sm1=y+sm1
    if sm1==sm:
        return True
n=eval(input())
if math.floor(n)==n and n>0:
    for m in range(n):
        if hws(m):
            if zs(m):
                print(m,end="")
else:
    print("illegal input")
