stu_list = [['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
num_list = [201801, 201802, 201803, 201804, 201805, 201806, 201807, 201808, 201809, 201810, 201811, 201812, 201813, 201814, 201815, 201816, 201817, 201818, 201819, 201820]
num1 = eval(input())
if 201800 < num1 < 201821:
    a = num_list.index(num1) # 确定位置
    List1 = stu_list[a]
    print(str(List1))
else:
    print("None")

