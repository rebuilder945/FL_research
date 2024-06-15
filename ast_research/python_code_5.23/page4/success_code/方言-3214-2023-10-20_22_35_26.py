list=eval(input())
n=len(list)
jl=[0 for i in range(n)]
for i in range(n):
    if list[i]==0:
        jl[i]=1
for j in range(n):
    if jl[j]:
        list.remove(0)
        list.append(0)
print(list)

