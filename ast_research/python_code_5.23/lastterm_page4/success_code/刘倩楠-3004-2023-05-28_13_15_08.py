def Num(n):
    list1 = []#确定一个空列表
    for x in range(3,n):#遍历3到n的数字
        if n % x == 0:#n可以整除x
            list1.append(1)#将x加入列表
    if sum(list1) == 0:
        return 1#n为素数
    else:
        return 0#n非素数
lst=eval(input())
save=[]
for x in lst:
    if su_shu(x)==1:
        save.append(x)
print(save)
