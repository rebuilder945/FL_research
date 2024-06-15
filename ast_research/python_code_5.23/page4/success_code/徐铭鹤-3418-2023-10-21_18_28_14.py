def maxsum(nums):
    b = []
    c = []
    for x in range(0,int(len(nums)/2)):
          b.append(nums.pop(nums.index(max(nums))))
          c.append(nums.pop(nums.index(max(nums))))
    return(sum(c))  
 





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

