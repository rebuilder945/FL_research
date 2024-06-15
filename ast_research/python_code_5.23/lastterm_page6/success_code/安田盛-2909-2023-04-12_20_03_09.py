def f(lst,n):
    b=0
    c=len(lst)-1
    while b<=c:
        mid=(b+c)//2
        if str(n)==lst[mid][0]:
            return(mid)
        elif n<int(lst[mid][0]):
            c=mid-1
        else:
            b=mid+1
    return -1









stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],

['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],

['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],

['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],

['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
n=eval(input())
mid=f(stu_list,n)
if mid==-1:
    print('None')
else:
    print(stu_list[mid][0]+stu_list[mid][1])





