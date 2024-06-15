L1=eval(input())
N,M=eval(input())
S=len(L1)
if N > S or M > S:
    print("error")
else:
    for x in range(len(L1)):
        if N <= x < M:
            del L1[x]
    print(L1)
