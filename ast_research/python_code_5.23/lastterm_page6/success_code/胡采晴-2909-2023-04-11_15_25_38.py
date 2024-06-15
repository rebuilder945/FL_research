def search_stu(stu_list,key):
    left=0
    right=len(stu_list)-1
    while(left<=right):
        aid=(left+right)//2
        if(int(stu_list[aid][0])==key):
            return aid
        elif key<int(stu_list[aid][0]):
            right=aid-1
        else:
            left=aid+1
    return -1
stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],

['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],

['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],

['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],

['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]

key= eval(input())
aid=search_stu(stu_list,key)
if aid == -1:
    str1="None"
else:
    str1=stu_list[aid][0]+stu_list[aid][1]
print(str1)





