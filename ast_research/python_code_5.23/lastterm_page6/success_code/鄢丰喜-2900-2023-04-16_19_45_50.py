from math import sqrt
def P(x):
    f = True
    i = 2
    while i <= sqrt(x):
        if x % i == 0:
            f = False
        i = i+1
    return f
def Q(x):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False
n = int(input())
icount = 0
m = 2
finlist=[]
while icount < n:
    if P(m) == True and Q(m) == True:
        finlist.append(m)
        icount += 1
    m += 1
count=0
for j in tuple(finlist):
    print("{finlist:6}".format(finlist=j),end="")
    count +=1
    if count % 10 == 0:
        print(end="\n")
