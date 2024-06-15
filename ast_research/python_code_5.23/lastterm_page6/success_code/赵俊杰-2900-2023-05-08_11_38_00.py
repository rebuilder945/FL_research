def P(x):
    f = True
    i = 2
    while i < int(x/2)+1:
        if x % i == 0:
            f = False
            break
        i = i+1
    return f
nums = eval(input())
fnlist=[]
for x in range(2,nums):
    if x != 1 and x != 0 and P(x) == True:
        fnlist.append(x)
    else:
        pass
fnlist2=[]
for s in fnlist:
    if str(s)==str(s)[::-1]:
        fnlist2.append(s)
    else:
        pass
t=""
for j in fnlist2:
    t=t+str(j)+" "
print(t)
