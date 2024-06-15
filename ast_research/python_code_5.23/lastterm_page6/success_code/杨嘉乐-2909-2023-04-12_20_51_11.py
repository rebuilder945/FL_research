def fu(l,key):
    left=0
    right=len(l)-1
    while(left<=right):
        mid=(left+right)//2
        if l[mid][0]==key:
            return mid
        elif key<int(l[mid][0]):
            right=mid-1
        else:
            left=mid+1
    return -1
stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],
['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],
['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],
['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],
['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
n=eval(input())
kao=fu(stu_list,n)
if kao==-1:
    print('None')
else:
    print(stu_list[kao][0]+stu_list[kao][1])
