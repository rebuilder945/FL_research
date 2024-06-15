def calDegrees(x):
    for i in x:
        list=[].append(x.count(i))
        return max(list)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

