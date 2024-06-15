shulie = eval(input())
shuliang = len(shulie)
zongshu = sum(shulie)
average = zongshu/shuliang
if average - zongshu//shuliang > 0:
    print("%.2f"%(average))
else:
    print("%d"%(average))
