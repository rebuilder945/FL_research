n=eval(input())
a=[(x+1)/x for x in range(n)]
b=0
for x in a:
    b=b+x
print(b)
