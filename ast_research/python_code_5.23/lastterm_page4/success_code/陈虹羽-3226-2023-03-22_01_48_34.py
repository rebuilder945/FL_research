def search(nums):
    a=[]
    for i in nums:
        if nums.count(i)>len(nums)//2:
            a.append(i)
    if a==[]:
        return False
    else:
        return i





nums = eval(input())
y = search(nums)
print(y)


