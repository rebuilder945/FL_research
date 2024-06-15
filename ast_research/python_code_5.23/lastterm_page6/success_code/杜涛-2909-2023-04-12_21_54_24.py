def search(lst,key):
    left=0
    right=len(lst)-1
    while left<=right:
        mid=(left+right)//2
        if int(lst[mid][0])==key:
            return mid
        elif int(lst[mid][0])>key:
            right=mid-1
        else :
            left=mid+1
    return -1
lst=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],
['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],
['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],
['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],
['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
key=eval(input())
mid=search(lst,key)
if mid==-1:
    a="None"
else :
    a=lst[mid][0]+lst[mid][1]
print(a)











# key=input()
# m=0
# for x in range(len(lst)):
#     if lst[x][0]==key:
#         m=1
#         print(lst[x][0]+lst[x][1])
# if m==0:
#     print("None")

