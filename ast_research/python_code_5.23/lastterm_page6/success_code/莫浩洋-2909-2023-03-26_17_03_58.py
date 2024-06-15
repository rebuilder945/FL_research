stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
n=eval(input())
front,ending = 0,len(stu_list)-1
a = 0
while front <= ending:
    mid = (front+ending)//2
    if stu_list[mid][0] ==str(n):
        print("{}{}".format(stu_list[mid][0],stu_list[mid][1]))
        a=1 
        break
    elif int(stu_list[mid][0]) >= n :
        ending = mid - 1
    else :
        front = mid + 1
if a != 1:
    print("None")

