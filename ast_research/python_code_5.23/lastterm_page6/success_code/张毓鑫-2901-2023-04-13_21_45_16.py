def p(a,b,c):
    if a!='#':
        b+=1
        c+=a
        a=eval(input())
        p(a,b,c)
    else:
        return b%c
a=eval(input())
b=0
c=0
d=p(a,b,c)
print(d)
