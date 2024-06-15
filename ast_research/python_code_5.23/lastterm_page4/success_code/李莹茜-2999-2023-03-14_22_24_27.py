biao=list(eval(input()))
n,m=input().split(" ")
biaoCopy1=biao.copy()
biaoCopy1[n]=biao[m]
biaoCopy2=biaoCopy1.copy()
biaoCopy2[m]=biao[n]
print(biaoCopy2)
