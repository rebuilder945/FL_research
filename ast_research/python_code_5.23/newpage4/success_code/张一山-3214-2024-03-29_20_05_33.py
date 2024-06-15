M=eval(input())
N=M.count(0)
for i in range(N):
    M.remove(0)
    M.append(0)
print(M)
