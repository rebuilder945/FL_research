from math import sqrt
def p(x):
    f = True
    i =2
    while i <= sqrt(x):
        if x % i ==0:
            f =False
            break
        i=i+1
    return f
nums =eval(input())
fnlist=[]
for x in nums:
    if x!=1 and x!=0 and p(x)==True:
        fnlist.append(x)
    else:
        pass
print(fnlist)
