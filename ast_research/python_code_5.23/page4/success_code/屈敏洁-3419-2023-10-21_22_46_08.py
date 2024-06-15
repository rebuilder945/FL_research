def calDegrees(nums):
    ls = []
    for i in nums:
        n = nums.count(i)
        ls.appent(n)
    m = max(ls)  
    return m; 


     
           


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

