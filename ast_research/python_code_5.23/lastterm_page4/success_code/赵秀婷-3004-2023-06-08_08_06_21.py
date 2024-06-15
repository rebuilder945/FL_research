#计算列表的度
# def calDegrees(nums):
#     blist=[]
#     for i in nums:
#         m=nums.count(i)
#         blist.append(m)
#         pmax=max(blist)
#     return pmax

# def calDegrees(nums):
#     maxvalue=0
#     for i in nums:
#         if(maxvalue>nums.count(i)):
#             maxvalue=nums.count(i)
#     return maxvalue
    
# nums = eval(input())
# d=calDegrees(nums)  #调用自定义函数
# print(d)

# 把数列的元素重复n次，然后元素的平方形成新列表，然后去除重复元素
# ls=eval(input())
# n=eval(input())
# ls2=ls*n
# ls3=[x*x for x in ls2]
# ls4=[]
# for i in ls3:
#    if(i not in ls4):
#       ls4.append(i)
# print(ls4)

# 把长度为2n的列表分成n对，使得每一对的最小值的和最大

# def maxsum(nums):
#     nums.sort()
#     ls=nums[::2]
#     m=sum(ls)
#     return m
# nums  =  eval(input())
# v  =  maxsum(nums)#调用自定义函数
# print(v)

# 编写函数获得第n项斐波那契数列的值
# def Fibonacci(num,n):
#     cun=num
#     for i in range(2,n):
#         cun.append(cun[-1]+cun[-2])
#     return cun[-1]
# num  =  [1,1]
# n  =  int(input())
# print(Fibonacci(num,  n))

# 找出不是两个列表中的共有元素，在结果列表升序没有重复元素
# nums1  =  eval(input())
# nums2  =  eval(input())
# nums3  =  []
# for x in nums1:     #  把不nums1中和nums2不重复的元素加入nums3
#     if x not in nums2:
#         if x not in nums3:
#             nums3.append(x)
# for x in nums2:     #  把num2中的元素不重复的加入nums3
#     if x not in nums1:
#         if x not in nums3:
#             nums3.append(x)
# nums3.sort()
# print(nums3)

# 找出列表中的多数元素 
# def search(nums):
#     for i in nums:
#         if (nums.count(i)>len(nums)//2) :
#             return i
#         else:
#             return False
# nums = eval(input())    
# y = search(nums)
# print(y)

# 把分布在两个列表中的姓名和成绩配对后形成一个列表
# a=input().split(",")
# b=eval(input())
# c=[]
# for i in range(0,len(b)):
#     temp=[]
#     temp.append(a(i))
#     temp.append(b(i))
#     c.append(temp)
# print(c)

# names=input().split(",")
# grades=eval(input())
# bond=[]
# for x in list(range(len(names))):
#     ml=[names[x],grades[x]]
#     bond.append(ml)
# print(bond)

# 生成指定长度的等差数列

# n,m,l=eval(input())
# s=n+(m-1)*l+1
# print(list(range(n,s,l)))

# 删除列表中指定位置的元素
# lst=eval(input())
# n,m=eval(input())
# nums=len(lst)
# if n not in range(0,nums) or m not in range(0,nums):
#     print("error")
# else:
#     # print(lst[:n]+lst[m:])      法一
#     del lst[n+1:m+1]          法二
#     print(lst)

# 找出自然数列表中的素数，并放入另外一个列表，然后输出找出的素数



def sushu(n):         
    if (n>=2) :
        for i in range(2,n):
            if (n%i==0):
                return False
            else:
                return  True
    else:
        return False


a=eval(input())
save=[]
for i in a:
    if (sushu(i)):
        save.append(i)
print(save)     
