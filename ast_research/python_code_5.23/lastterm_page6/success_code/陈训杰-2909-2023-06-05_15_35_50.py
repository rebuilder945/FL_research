stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],
['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],
['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],
['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],
['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
low=0
high=len(stu_list)-1
k= -1
m=eval(input())
for i in stu_list:
    while low <= high:
        mid = (low+high)//2
        n=stu_list[mid]
        if m < int(n[0]):
            high=mid-1
        else:
            if m > int(n[0]):
                low = mid+1
            else:
                k=int(n[0])
                break
if k > 0:
    print(n[0],end='')
    print(n[1])
else:
    print("None")
