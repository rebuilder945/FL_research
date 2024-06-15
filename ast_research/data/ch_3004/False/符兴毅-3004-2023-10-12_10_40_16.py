a = eval(input())
aim = []
for nums in a:
    if nums==1:
        break
    for i in range(2,nums):
        if nums%i==0:
            break
    else:
        aim.append(nums)
print(aim)
