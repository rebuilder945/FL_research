nums=eval(input())
nums.sort(reverse=True)
if nums.count(0)!=len(nums):
    for x in nums:
        print(x,end=(""))
else:
    pass
    print("0")
