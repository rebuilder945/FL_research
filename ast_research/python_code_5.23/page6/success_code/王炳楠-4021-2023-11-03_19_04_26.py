l1=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],['201813','zhaoyi'],['201814','zhaoer'],['20181','zhaosan'],['201816','zhaosi'],['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
l2=[l1[i][0] for i in range(len(l1))]
def binary_search(stu_list, target):
    left = 0
    right = len(stu_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if eval(stu_list[mid][0]) == target:
            return stu_list[mid]
        elif eval(stu_list[mid][0]) > target:
            right = mid
        else:
            left = mid
  

target = eval(input())
if str(target) not in l2:
    print("None")

else:
    lie=binary_search(l1,target)
    print(lie[0]+lie[1])

