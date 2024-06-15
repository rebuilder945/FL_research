def calDegrees(nums):
    dic={}
    for i in nums:
        dic[i]=dic.get(i,0)+1
    max_count=0
    for x,y in dic:
        max_count=max(max_count,y)
    return max_count
    


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

