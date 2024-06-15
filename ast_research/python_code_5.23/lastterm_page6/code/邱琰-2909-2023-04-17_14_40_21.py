stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
def search(a,value):
    start,end=0,len(a)-1
    while start<=end:
        mid=(start+end)//2
        if a[mid][0]==value:
            return mid
        elif a[mid][0]>value:
            end=mid-1
        else:
            start=mid+1
    return None
sid=input()
index=search(stu_list,sid)
if index is None:
    print('None')
else:
    print(''join(stu_list[index]))
