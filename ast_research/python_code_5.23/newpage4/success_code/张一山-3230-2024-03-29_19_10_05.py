M=eval(input())
M.sort(reverse=True)
N=set(M)
for x in N:
    print(x,end="")
