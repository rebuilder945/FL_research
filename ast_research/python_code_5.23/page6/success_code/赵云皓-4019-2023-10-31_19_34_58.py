def nmsl(a):
    a=int(a)
    a=a+5
    b=a%10
    return b
a=list(input())
b=list(map(nmsl,a))
c=list(map(str,b))
c.reverse()
print("".join(c))
