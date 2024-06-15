#第一种：
def maxsum(nums):
    b = []
    c = []
    for x in range(0,int(len(nums)/2)):
        b.append(nums.pop(nums.index(max(nums))))
        c.append(nums.pop(nums.index(max(nums))))
    return(sum(c))  
 
nums  =  eval(input())
v  =  maxsum(nums)#调用自定义函数
print(v)
#第二种：
def maxsum(nums):
    n=len(nums)
    c=0
    nums.sort(reverse=True)
    for x in range(1,n+1,2):
          c=c+nums[x]
    return c
 




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

