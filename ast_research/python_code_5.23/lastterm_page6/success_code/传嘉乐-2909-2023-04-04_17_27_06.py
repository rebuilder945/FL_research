def s_s(stu_list,a):
    le=0
    r=len(stu_list)-1
    while (le<=r):
        m=(le+r)//2
        if a==int(stu_list[m][0]):
            return m
        elif a<int(stu_list[m][0]):
            r=m-1
        else:
            le=m+1
    return -1
stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
a=eval(input())
m=s_s(stu_list,a)
if m==-1:
    str1="None"
else:
    str1=stu_list[m][0]+stu_list[m][1]
print(str1)
