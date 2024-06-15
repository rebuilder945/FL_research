M=eval(input())
M.sort(reverse=True)
for x in M:
    if x==0:
        print("0")
    else:
        print(x,end="")
