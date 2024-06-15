nums = eval(input())
for x in nums:
    if x>2:
        for y in range(2,x):
            if x%y==0:
                nums.remove(x)
    elif x==1:
        nums.remove(x)
    elif x==0:
        nums.remove(x)
    else:
        pass
print(nums)
