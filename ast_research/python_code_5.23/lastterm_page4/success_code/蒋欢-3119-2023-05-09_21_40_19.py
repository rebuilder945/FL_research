import copy
def single(n):
    m=copy.deepcopy(n)
    for x in n:
        if m.count(x)>1:
            m.remove(x)
    print(m)
n=eval(input())
single(n)
