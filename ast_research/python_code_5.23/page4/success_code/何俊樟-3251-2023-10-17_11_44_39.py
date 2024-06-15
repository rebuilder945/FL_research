nums1 = eval(input())
nums2 = eval(input())
nums3 = []
# 把不nums1中和nums2不重复的元素加入nums3
for x in nums1:
    if x not in nums2:
        if x not in nums3:
                        if b or x!=a:
                            nums3.append(x)
                            b,a=0,x



# 把num2中的元素不重复的加入nums3
for x in nums2:
    if x not in nums1:
        if x not in nums3:
            nums3.append(x)
            if c or x!=d:
                nums3.append(x)
                c,d=0,x



print(nums3)


