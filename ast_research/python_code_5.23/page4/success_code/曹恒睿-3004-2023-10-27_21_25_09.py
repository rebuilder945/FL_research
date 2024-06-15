shulie=eval(input())
xinshulie=[]
feisushu=[]
for x in shulie:
    for i in range(2,x):
        if x%i==0:#x不是素数
            feisushu.append(x)
            break
        else:
            pass
for x in shulie:
    if x not in feisushu:
        xinshulie.append(x)
    else:
        pass        
print(xinshulie)

        


