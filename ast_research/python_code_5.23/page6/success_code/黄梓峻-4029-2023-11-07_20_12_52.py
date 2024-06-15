n,m=eval(input()).split("")
nums=[]
nums1=[]
if n>m or (n-int(n))>0 or (m-int(m))>0:
    print("illegal input")
else:
    for i in range(n,m):
        nums.append(i)
    for a in len(nums):
        for b in len(nums):
            for c in len(nums):
                if a!=b and b!=c and a!=c and nums[a]!=0:
                    s=str(nums[a])+str(nums[b])+str(nums[c])
                    if s not in nums1:
                        nums1.append(str(s))
                        print(' '.join(nums1))
                    else:
                        print("illegal input")
                else:
                    print("illegal input")
                  

