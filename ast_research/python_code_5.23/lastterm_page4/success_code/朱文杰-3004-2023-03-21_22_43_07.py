nums=eval(input())
for x in nums[:len(nums)]:
    for d in range(2,x):
        if x%d==0:
            nums.remove(x)
print(nums)
