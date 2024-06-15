def search(nums):
    jack=[]
    for i in nums:
        a=nums.count(i)
        jack.append(a)
        b=max(jack)   
        if b>len(nums)//2:
            y=i
        else:
            y='False'
    return(y)





nums = eval(input())
y = search(nums)
print(y)


