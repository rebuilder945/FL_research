a = list(eval(input()))
b = sorted(a,reverse=True)
if b[0] in "0":
    print(0)
else:
    for i in b:
        print(i,end="")
