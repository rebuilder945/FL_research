nums1 = eval(input())
nums2 = eval(input())
nums3 = []
# 把不nums1中和nums2不重复的元素加入nums3
for x in nums1:
    if x not in nums2:
        if x not in nums3:
            num3+=[x]



# 把num2中的元素不重复的加入nums3
for x in nums2:
    if x not in nums1:
        if x not in nums3:
            nums3.append(x)
num3=list(set(num3))
x=len(num3)
for i in range(x):
    for j in range(x-i-1):
        if num3[j]>num3[j+1]:
            num3[j],num3[j+1]=num3[j+1],num3[j]




print(nums3)


