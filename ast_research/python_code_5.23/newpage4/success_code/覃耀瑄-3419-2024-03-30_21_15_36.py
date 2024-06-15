def calDegrees(inter_list):
    maxCnt = 0
    ls = []  # 存放已经统计过的数字
    for v in inter_list:
        if v not in ls: # 跳过已经统计过的数字
            ls.append(v) # 将数字插入新列表
            k = inter_list.count(v) # 统计v出现的次数
            if k > maxCnt: # 比较次数，并更新最大次数
                maxCnt = k
    return maxCnt



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

