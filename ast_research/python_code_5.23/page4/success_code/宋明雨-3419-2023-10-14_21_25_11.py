def calDegrees(list):
    List = []
    for i in list:
        N = list.count(i)
        List.append(N)
        M = max(List)
    return M



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

