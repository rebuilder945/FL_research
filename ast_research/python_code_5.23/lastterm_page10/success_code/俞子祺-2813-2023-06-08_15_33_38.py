n=input()
m=input()
n=list(n)
if m in n:
    n.remove(m)
    print("".join(n))
else:
    print("".join(n))
    
