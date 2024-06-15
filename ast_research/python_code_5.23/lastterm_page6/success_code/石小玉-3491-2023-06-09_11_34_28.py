def shift(lst):
    x=len(nums)
    y=nums[x-1]
    del nums[-1]
    nums.append(y)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

