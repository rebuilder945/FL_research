nums = list(map(int,input().split(",")))
n, m = input().split(",")
if int(n) > int(len(nums)) - 1 or int(n) < int(-len(nums)):
    print("error")
else:
    ls = nums + [nums[int(n)]]*int(m)
    print(ls)    

