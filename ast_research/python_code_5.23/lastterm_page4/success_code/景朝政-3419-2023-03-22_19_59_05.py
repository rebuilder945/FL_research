def calDegrees(li):
    dic = {}
    for v in li:
        if v in dic.keys():
            dic[v] += 1
        else:
            dic[v] = 1
    return max(dic.values())


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

