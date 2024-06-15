a = list(eval(input()))
b = sorted(a,reverse=True)
for i in b:
    if b[0]==0:
        print(0)
    else: 
        print(i,end="")
