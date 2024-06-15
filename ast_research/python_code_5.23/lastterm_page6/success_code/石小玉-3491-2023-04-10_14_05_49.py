def shift(lst):
    iA=int(input())
    nums=list(range(1,iA+1,1))
    a=nums[0]
    nums.remove(a)
    nums.append(a)
print(nums)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

