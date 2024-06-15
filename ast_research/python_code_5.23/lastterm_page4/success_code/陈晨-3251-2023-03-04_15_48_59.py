nums1 = eval(input())
nums2 = eval(input())
nums3 = []
# 把不nums1中和nums2不重复的元素加入nums3
for x in nums1:
    if x not in nums2:
        if x not in nums3:
            nums3.append(x)



# 把num2中的元素不重复的加入nums3
for x in nums2:
    if x not in nums1:
        if x not in nums3:
            nums3.append(x)
for x in nums3:
    while nums3.count(x)>1:
        nums3.remove(x)
nums3.sort()



print(nums3)


