stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
target=eval(input())
left=0
right=len(stu_list)
while left<right:
    middle=(left+right)//2
    nums=int(stu_list[middle][0])
    if nums<target:
        left=middle+1
    elif nums>target:
        right=middle
    else:
        print(stu_list[middle][0]+stu_list[middle][1])
        break
else:
    print(None)
