a=eval(input())
a.sort(reverse=True)
s=""
for x in a:
    if x==0:
        s=0
    else:
        s=s+str(x)


print(s)





