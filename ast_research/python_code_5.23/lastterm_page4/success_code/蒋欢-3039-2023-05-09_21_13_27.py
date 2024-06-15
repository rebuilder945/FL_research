def deTip(n):
    n=list(set(n))
    n.remove(max(n))
    n.remove(min(n))
    print(n)
n=eval(input())
deTip(n)
