nums=eval(input())
for x in nums[:len(nums)]:
    if x<2:
        nums.remove(x)
    else:
        for d in range(2,x):
            if x%d==0:
                nums.remove(x)
print(nums)
