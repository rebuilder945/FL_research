n=input()
m=input()
n=list(n)
if m in n:
    n.remove(m)
    n=str(n)
    print(n)
else:
    n=str(n)
    print(n,end="")
    
    
