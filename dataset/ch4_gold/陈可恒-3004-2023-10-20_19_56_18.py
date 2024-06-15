a = eval(input())
b = []
for x in range(len(a)):
    flag = True
    if a[x]==1 or a[x]==0:
        flag = False
    for s in range(2,a[x]):
        if a[x]%s==0: #不是素数
            flag = False
            break
    if flag == True:
        b.append(a[x])
print(b)
