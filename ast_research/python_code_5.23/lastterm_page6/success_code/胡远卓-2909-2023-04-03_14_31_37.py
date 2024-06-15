tu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],
['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],
['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],
['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],
['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
id=eval(input())
l=0
r=20
while l+1<r:
    mid=(l+r)//2
    num=int(tu_list[mid][0])
    if num<=id:
        l=mid
    else:
        r=mid
res=int(tu_list[l][0])
if res==id:
    print("%s%s"%(tu_list[l][0],tu_list[l][1]))
else:
    print("None")
