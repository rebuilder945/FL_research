stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
find=int(input())
left=0
right=int(len(stu_list))
if 201801<=find<=201820:
    while left<=right:
        mid=(left+right)//2
        if int(stu_list[mid][0])>find:
            right=mid
        elif int(stu_list[mid][0])<find:
            left=mid
        elif int(stu_list[mid][0])==find:
            print("%s%s"%(stu_list[mid][0],stu_list[mid][1]))
            break
else:
    print("None")
