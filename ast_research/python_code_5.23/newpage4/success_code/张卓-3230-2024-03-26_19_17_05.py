a = list(eval(input()))
b = sorted(a,reverse=True)
for i in b:
    if i==0:
        print(0)
    else:
        print(i,end="")
