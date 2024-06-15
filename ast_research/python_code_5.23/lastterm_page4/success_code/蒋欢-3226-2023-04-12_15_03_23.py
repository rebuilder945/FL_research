def search(nums):
    t=[]
    for n in nums:
        m=nums.count(n)
        t.append(m)
    if max(t)>len(nums)//2:
        return nums[t.index(max(t))]
    else:
        return "False"





nums = eval(input())
y = search(nums)
print(y)


