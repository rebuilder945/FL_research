stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],

['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],

['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],

['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
number=eval(input())
number1=number-201801
def find(ls,n):
    low=0
    high=len(ls)
    while low<high:
        if number1%2!=0:
            mid=int((low+high-1)/2)
        elif number1%2==0:
            mid=int((low+high)/2)
        if mid==n:
            return ls[mid][0]+ls[mid][1]
        elif mid>n:
            high=mid-1
        else:
            low=mid+1
    if low==high:
        if number1==low:
            return ls[low][0]+ls[low][1]
    return False
if find(stu_list,number1) is False:
    print("None")
else:
    print(find(stu_list,number1))
