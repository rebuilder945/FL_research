l1 = eval(input())
# 拷贝列表
l2 = l1.copy()




l1.sort()
l2.sort(reverse=True)
l3 = l1 + l2
# 把偶数位置的元素设置为0
for x in list(range(len(l3))):
    if x % 2 == 0:
        l3[x]=0
    else:
        pass
    




print(l3)



