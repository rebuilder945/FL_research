n=eval(input())
b=max(n)
c=min(n)
while b in n:
    n.remove(b)
    break
while c in n:
    n.remove(c)
    break
print(n)
