a = eval(input())
aim = []
for nums in a:
    for i in range(2,nums):
        if nums%i==0:
            break
    else:
        aim.append(nums)
print(aim)
