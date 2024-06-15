n=eval(input())
def yi(b):
    t=[i for i,x in enumerate(b) if x==0]
    l=[ i for i, x in enumerate(b) if x !=0]
    if l == []:
        return b
    else:
        for i in reversed(t):
            b.insert(l[-1], b.pop(i))
    return b

print(n)

