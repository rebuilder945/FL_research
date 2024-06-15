a=list(input())
b=input()
c=a.count(b)
if c==0:
    print("".join(a))
else:
    for x in range(c):
        a.remove(b)
    print("".join(a))

        
