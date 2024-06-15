m=list(eval(input()))
m.sort(reverse=True)
for x in m:
    if x==0:
        print(0)
    else:
        print(x,end="")
    
