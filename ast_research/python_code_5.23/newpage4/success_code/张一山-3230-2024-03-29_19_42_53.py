M=eval(input())
M.sort(reverse=True)
for x in M:
    if x==0:
        print(x,end="")
    else:
        print("0")
