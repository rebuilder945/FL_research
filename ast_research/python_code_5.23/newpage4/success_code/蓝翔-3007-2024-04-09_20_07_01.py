nums1 = eval(input())
a,b = eval(input())
c = int(a)
d = int(b)
if c in nums1 and d in nums1:
    if c<d :
        i = set(range(c+1,d+1,1))
        nums2 = set(nums1) 
        n = nums2 ^ i
        print(list(n))
    else:
        j = set(range(d+1,c+1,1))
        nums3 = set(nums1)
        m = nums3 ^ j
        print(list(m))
else:
    print("error")
