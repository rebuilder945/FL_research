stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],

['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],

['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],

['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],

['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
num=eval(input())
left=0
right=len(stu_list)-1
while left <= right:
    middle=(left+right)//2
    if int(stu_list[middle][0])<num:
        left=middle+1
    if int(stu_list[middle][0])>num:
        right=middle-1
    if int(stu_list[middle][0])==num:
        print(stu_list[middle][0]+stu_list[middle][1])
        break
else:
    print(None)
