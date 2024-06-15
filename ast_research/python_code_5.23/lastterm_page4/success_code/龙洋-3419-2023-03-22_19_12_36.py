def calDegrees(nu):
    Lis=[nu.count(x) for x in nu]
    print(max(Lis))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

