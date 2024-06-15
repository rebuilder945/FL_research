up=[2,3]
dowm=[1,2]
total=0
n=int(input())
for i in range(1,n+1):
    up.append(up[i-1]+up[i])
    dowm.append(dowm[i-1]+dowm[i])
for j in range(n):
    total+=up[j]/dowm[j]
print('%.4f'%total)
