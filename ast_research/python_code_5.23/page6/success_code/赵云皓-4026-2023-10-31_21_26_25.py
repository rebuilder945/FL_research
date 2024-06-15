n=eval(input())
a=[(x+2)/(x+1) for x in range(n)]
b=0
for x in a:
    b=b+x
print("%.4f"%b)
