nums = input().split(",")
grades = eval(input())
lst1=[]
lst2=[]
for i in range(len(nums)):
    lst1 = [nums[i],grades[i]]
    lst2.append(lst1)
    lst1 = []
print(lst2)
