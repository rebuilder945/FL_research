nums1  =  eval(input())
nums2  =  eval(input())
nums3  =  []
#  把不nums1中和nums2不重复的元素加入nums3
for  x  in  nums1:
        if  x  not  in  nums2:
                if  x  not  in  nums3:
                        
                        nums3.append(x)




a=input().split(',')
b=eval(input())
a=list(a)
m=[]
for i in range(len(a)):
    n=[]
    n.append(a[i])
    n.append(b[i])
    m.append(n)
print(m)

