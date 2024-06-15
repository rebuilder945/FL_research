def calDegrees(list):
    cubes = [list.count(x) for x in list]
    return max(cubes)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

