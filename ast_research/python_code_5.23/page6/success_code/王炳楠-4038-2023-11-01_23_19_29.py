ls=list(input())
a=0
b=0
c=0
d=0
for x in ls:
    if ord(x) in range(65,91) or ord(x) in range(97,123):
        a=a+1
    elif x==" ":
        b=b+1
    elif ord(x) in range(48,58):
        c=c+1
    else:
        d=d+1
print(a,b,c,d)
