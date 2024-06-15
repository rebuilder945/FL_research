def calDegrees(nums):
    count_dict={}
    for i in nums:
        if i in count_dict:
            count_dict[i]+=1
        else:
            count_dict[i]=1
    max_count=max(count_dict.values())
    max_elements=[i for i,j in count_dict.items() if j==max_count]
    return max_elements


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

