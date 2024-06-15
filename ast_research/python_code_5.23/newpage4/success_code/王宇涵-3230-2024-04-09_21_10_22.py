nums= eval(input())
nums.sort(reverse=True)
if nums[0]==0:
        print(0)
else:
    for x in nums:
     print(x,end='')

