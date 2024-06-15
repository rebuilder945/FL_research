def calDegrees(nums) :
    list=[]
    for i in range(len(nums)) :
        m=1
        for n in range(len(nums)-i) :
            if nums[i]==nums[i+n] :
                m += 1
        list.append(m) 
    for data in list :
         for s in range(len(list)) :
             if data >= list[s] :
                d=data
    return d


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

