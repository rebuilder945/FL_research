n=eval(input())
def yi(n):
    t=[i for i,x in enumerate(n)]
    for i in reversed(t):
        n.insert(len(n), n.pop(i))
    return n
print(yi(n))
