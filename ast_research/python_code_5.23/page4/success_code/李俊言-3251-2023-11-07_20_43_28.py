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
for s in range(len(nums3)-1,0,-1):
      for x in range(s):
           if nums3[x]>nums3[x+1]:
                 nums3[x],nums3[x+1]=nums3[x+1],nums3[x]
                
           



print(nums3)


