def search(nums):
    m=[]
    for i in nums:
        if nums.count(i)>len(nums)//2:
            nums.append(i)
        else:
            print("False")






nums = eval(input())
y = search(nums)
print(y)


