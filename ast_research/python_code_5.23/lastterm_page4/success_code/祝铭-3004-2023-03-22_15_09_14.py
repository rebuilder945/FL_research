nums = eval(input())
for x in nums:
    if x>7:
        if x%2==0 or x%3==0 or x%5==0 or x%7==0:
            nums.remove(x)
    elif x==1 or x==4 or x==6 or x==0:
        nums.remove(x)
print(nums)
