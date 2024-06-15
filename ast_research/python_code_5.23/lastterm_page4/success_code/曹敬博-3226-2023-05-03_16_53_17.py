def search(nums):
    n=len(nums)
    candidate=nums[0]
    count=0
    for i in range(n):
        if nums[i]==candidate:
            count+=1
        else:
            count-=1
            if count==0:
               candidate=nums[i+1]
        return candidate if nums.count(candidate)>n//2 else None





nums = eval(input())
y = search(nums)
print(y)


