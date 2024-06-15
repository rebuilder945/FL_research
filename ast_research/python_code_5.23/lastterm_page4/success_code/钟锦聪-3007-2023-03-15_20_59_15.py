nums = eval(input())
n,m=eval(input())
b = len(nums)
if n <=b-1 and m <= b-1:
    for x in range(n,m):
        del nums[n]
    print(nums)
else:
    print("error")
