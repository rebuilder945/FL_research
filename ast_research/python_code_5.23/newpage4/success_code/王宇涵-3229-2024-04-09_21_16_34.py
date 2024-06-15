nums = eval(input())
nums1=[]
for x in nums:
    if not nums.count(x)==1:
        print(False)
    elif nums.count(x)==1:
        nums1.append(x)
nums1.sort()



