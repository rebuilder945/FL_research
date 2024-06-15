a = eval(input())
if a == []:
    print([])
else:
    # 找出最大值和最小值
    m = max(a)
    n = min(a)
    # 计算最大值和最小值在列表中的出现次数
    maxi = a.count(m)
    minn = a.count(n) 
    # 删除多余的最大值和最小值
    for i in range(maxi):
        a.remove(m)
    for i in range(minn):
        a.remove(n)
    # 输出结果
    print(a)
