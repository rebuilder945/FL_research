lst = [['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],

['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],

['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],

['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],

['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
n = eval(input())
if n<=201800 or n>=201821:
    print("None")
else:
    left = 0
    right = len(lst)-1
    while left<=right:
        mid = (left+right)//2
        if int(lst[mid][0]) == n:
            s = lst[mid][0]+lst[mid][1]
            print(s)
            break
        elif n<int(lst[mid][0]):
            right = mid-1
        else:
            left = mid+1

