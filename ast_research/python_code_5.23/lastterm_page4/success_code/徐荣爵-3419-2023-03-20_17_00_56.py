record=[]
def calDegrees(nums):
        for x in nums :
            add = nums.count(x)
            record.append(add)
        return max(record)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

