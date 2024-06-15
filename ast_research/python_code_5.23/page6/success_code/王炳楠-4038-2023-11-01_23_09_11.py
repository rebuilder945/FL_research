ls=list(input())
a=0
b=0
c=0
d=0
for x in ls:
    if chr(x) in range(65,123):
        a=a+1
    elif x==" ":
        b=b+1
    elif eval(x) in range(0,10):
        c=c+1
    else:
        d=d+1
print(a,b,c,d)
