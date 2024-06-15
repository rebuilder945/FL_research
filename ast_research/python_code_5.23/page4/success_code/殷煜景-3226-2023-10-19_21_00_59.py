def search(nums):
    for i in nums:
        if nums.count(i)>len(nums)//2:
            m=i
            return i
        else:
            continue
    if not m:
        print("False")





nums = eval(input())
y = search(nums)
print(y)


