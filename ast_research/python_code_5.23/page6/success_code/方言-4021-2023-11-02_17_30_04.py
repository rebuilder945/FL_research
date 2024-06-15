k=input()
left=0
right=19
m=int((left+right)/2)
stu=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],
['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],
['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],
['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],
['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
while left<=right:
    print(left,right,m)
    if not "201801"<=k and k<="201820":
        print("None")
        break
    elif stu[m][0]<k:
        left=m-1
        m=int((left+right)/2)
    elif stu[m][0]>k:
        right=m+1
        m=int((left+right)/2)
    else:
        print(stu[m][0]+stu[m][1])
        break
