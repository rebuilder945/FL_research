stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
a=eval(input())
if a>201810 and a<201821:
    for i in range(11,int(len(stu_list)/2+10)):
        if a==eval(stu_list[i][0]):
            print(*stu_list[i],sep="")
if a<=201810 and a>=201801:
    for i in range(0,int(len(stu_list)/2)):
        if a==eval(stu_list[i][0]):
            print(*stu_list[i],sep="")
else:
    print(None)
