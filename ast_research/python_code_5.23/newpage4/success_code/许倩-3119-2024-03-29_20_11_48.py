# 2
# nums1=eval(input())
# nums2=[]
# for x in nums1:
#     if nums1.count(x)==1:
#         nums2.append(x)
# nums2.sort()
# if len(nums2)==0:
#     print('False')
# else:
#     str1=','.join(map(str,nums2))
#     print(str1)

# 3
# a=eval(input())
# s=a.count(0)
# while a.count(0)>=1:
#     a.remove(0)
# c=[0]*s
# a=a+c
# print(a)

# 4
# n=eval(input())
# sums=range(1,n+1)
# sums2=[]
# m=sums[0]
# for i in range(len(sums)-1):
#     sums2.append(sums[i+1])
# sums2.append(m)
# print(sums2)

# 5
from audioop import reverse


list1=eval(input())
list1.reverse()
list2=[]
for i in list1:
    if i not in list2:
        list2.insert(0,i)
print(list2)

# 6
# a=eval(input())
# b=max(a)
# c=min(a)
# d=a.copy()
# for x in a:
#     if x==b or x==c:
#         d.remove(x)
# print(d)


# 第七题
# names=input().split(",")
# scores=eval(input())
# a=[]
# for x in range(len(names)):
#     a.append([names[x],scores[x]])
# print(a)

# 第八题
# n,m,l=map(int,input().split(','))
# array=[n]
# for i in range(m-1):
#     n=n+l
#     array.append(n)
# print(array)

# 第九题
# lst=eval(input())
# n,m=map(int,input().split(','))
# if n<len(lst) and len(lst)>m>=n:
#     del lst[n:m]
#     print(lst)
# else:
#     print('error')

# 第十题
# def sushu(y):
#     x=[]
#     for i in y:
#         if i>=2:
#             for j in range(2,i,1):
#                 if i%j==0:
#                     break
#             else:
#                 x.append(i)
#     print(x)
# sums=eval(input())
# sushu(sums)

# 第十一题
# nums=eval(input())
# a=sum(nums)/len(nums)
# a_int=int(a)
# if a>a_int:
#     print('%.2f'%a)
# else:
#     print(a_int)

# 第十二题
# a=eval(input())
# b=sum(a)/len(a)
# print('%.2f'%b)

# 13
# a=input().split()
# n,m=map(int,input().split())
# b=a[n]
# a[n]=a[m]
# a[m]=b
# print(a)

# 14
# mylist=list(eval(input()))
# n,m=eval(input())
# if n>0 and n>=len(mylist):
#     print('error')
# elif n<0 and abs(n)>len(mylist):
#     print('error')
# else:
#     temp=[mylist[n]]*m
#     mylist=mylist+temp
#     print(mylist)
