stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],
['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],
['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],
['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
begin,end=0,len(stu_list)
n1=eval(input())
while begin<=end:
    mid=(begin+end)//2
    if int(stu_list[mid][0])==n1:
        print(n1,stu_list[mid][1],sep="")
        break
    elif n1>int(stu_list[mid][0]):
        begin=mid+1
    elif n1<int(stu_list[mid][0]):
        end=mid-1
else:
    print("None")





