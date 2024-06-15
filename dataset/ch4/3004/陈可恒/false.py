a = eval(input())
b = []
for x in range(len(a)):
    flag = True
    for s in range(2,a[x]):
        if a[x]%s==0: #不是素数
            flag = False
            break
    if  a[x]==0 or 1:
        flag = False
    if flag == True:
        b.append(a[x])
print(b)
