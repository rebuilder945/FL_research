M=eval(input())
M.sort(reverse=True)
sum=""
for i in range(len(M)):
    sum+=str(M[i])
print(int(sum))
