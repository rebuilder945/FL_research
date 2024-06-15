stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],

['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],

['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],

['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],

['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
find=input()
a=[]
for i in range(20):
    a.append(stu_list[i][0])
    a.append(stu_list[i][1])
if find in a:
    b=a.index(find)
    print("%s%s"%(a[b],a[b+1]))
else:
    print("None")
