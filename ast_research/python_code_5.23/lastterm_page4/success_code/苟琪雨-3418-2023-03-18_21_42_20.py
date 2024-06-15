def maxsum(a_list):
    min_max = 0
    a_list.sort()
    
    for i in range(0,len(a_list),2):
        min_max += a_list[i]
        
    return min_max




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

