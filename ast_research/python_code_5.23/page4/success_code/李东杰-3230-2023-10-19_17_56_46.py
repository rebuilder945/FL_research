a=eval(input())
a.sort(reverse=True)
s=""
for x in a:
    b=a.count(0)
    if len(a)==b:
        print(0)
        
    else:
        s=s+str(x)


print(s)





