import copy
def deTip(n):
    m=copy.deepcopy(n)
    for x in n:
        if x==max(n) or x==min(n):
            m.remove(x)
        else:
            continue
    print(m)
n=eval(input())
deTip(n)    
