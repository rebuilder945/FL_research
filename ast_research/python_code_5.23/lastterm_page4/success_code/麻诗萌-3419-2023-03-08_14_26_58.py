def calDegrees(nums) :
    list=[]
    for i in range(len(nums)) :
        m=0
        for n in range(len(nums)-i) :
            if nums[i]==nums[i+n] :
                m += 1
        list.append(m) 
    d=max(list)
    return d


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

