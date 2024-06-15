m=list(eval(input()))
m.sort(reverse=True)
if m[0]==0:
    print("0")
else:
    for x in m:
        print(x,end="")
