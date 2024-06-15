n=eval(input())
def yi(n):
    t=[i for i,x in enumerate(n) if x==0]
    l=[ i for i, x in enumerate(n) if x ==0]
    for i in reversed(t):
        n.insert(l[-1], n.pop(i))
    return n
n=yi(n)
print(n)
