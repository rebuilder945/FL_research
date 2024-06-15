def select(list1,i):
    left = 0
    right = len(list1)-1
    while left <= right:
        mid = (left+right)//2
        if int(list1[mid][0])==i:
            return list1[mid]

        elif i > int(list1[mid][0]):
            left = mid+1
        else:
            right = mid-1
    return -1
list1 = [['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],

['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],

['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],

['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],

['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
i = eval(input())
if select(list1,i)== -1:
    print("None")
else:
    print(*select(list1,i),sep='')

   
    

    

