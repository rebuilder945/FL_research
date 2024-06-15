def calDegrees(a:list):
    maxNum = 0
    for x in a:
        temp = a.count(x)
        if temp>maxNum:
            maxNum=temp
    
    return maxNum



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

