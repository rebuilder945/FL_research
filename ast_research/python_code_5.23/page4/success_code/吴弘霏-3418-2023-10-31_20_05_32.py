def maxsum(nums):
    a=[]
    b=len(nums)
    c=[]
    for i in range(0,int(b/2)+1):
        if i not in a:
            nums.remove(max(nums))
            c.append(max(nums))
    return sum(c)

        
        




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

