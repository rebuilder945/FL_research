def maxsum(nums):
    a = 0
    nums.sort(reverse=True)
    list1 = []
    for i in range(0,len(nums)//2):
        b = nums[2*i+1]
        list1.append(b)
    for i in range(0,len(list1)):
        c = list1[i]
        a = c + a   
    return(a)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

