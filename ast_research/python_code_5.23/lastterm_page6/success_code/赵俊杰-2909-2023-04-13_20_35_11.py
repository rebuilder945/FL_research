def mid(stu_list,key):
    mid=len(stu_list)//2
    left=0
    right=len(stu_list)
    while left<=right:
        if key==int(stu_list[mid][0]):
            return stu_list[mid][1]
        elif key<int(stu_list[mid][0]):
            right=mid
            mid=mid//2
        else:
            left=mid
            mid=(right+mid)//2
    return -1
stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
key=eval(input())
mid=int(mid(stu_list,key))
if mid==-1:
    str1="None"
else:
    str1=stu_list[mid][0]+stu_list[mid][1]
