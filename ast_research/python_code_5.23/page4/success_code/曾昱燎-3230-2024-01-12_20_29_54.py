def max_(nums):
    nums.sort()
    num=''
    for i in range(len(nums)-1,-1,-1):
        if nums[i] not in num:
            num+=str(nums[i])
    return int(num)
s=input()
print(int(s))

