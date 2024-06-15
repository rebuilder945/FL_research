M=eval(input())
M.sort(reverse=True)
for x in M:
    print(set(x),end="")
