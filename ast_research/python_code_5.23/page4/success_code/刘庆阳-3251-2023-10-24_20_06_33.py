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
n = 1
if n !=len(nums3):
    if  nums3[n-1]>nums3[n] and n!=1:
        nums3[n-1]=nums3[n]
        n-=1
    elif nums3[n-1]>nums3[n] and n==1:
        nums3[n-1]=nums3[n]
    else:
        n+=1
nums3.sort(reverse=True)



print(nums3)


