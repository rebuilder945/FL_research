bst=[]
def calDegrees(nums):
       for i in nums:
             bst.append(nums.count(i))
       return(max(bst))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

