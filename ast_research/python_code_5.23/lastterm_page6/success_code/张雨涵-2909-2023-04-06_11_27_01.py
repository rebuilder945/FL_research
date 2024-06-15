def halffind(stu_list,a):
    left = 0
    right = len(stu_list)-1
    while (left<=right):
        mid = (right + left)//2
        if a == int(stu_list[mid][0]):
            return mid
        elif a<=int(stu_list[mid][0]):
            right = mid -1
        else:
            left = mid+1
    else:
        return -1
a = eval(input())
stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
b = halffind(stu_list,a)
if b == -1:
    str = "None"
else:
    str = stu_list[b][0]+stu_list[b][1]
print(str)
