# 折半查找.1个列表里存储了20个子列表,各子列表内存储了学生的学号及姓名两个元素,两个元素都是字符串类型。 
# 现已知该 20 个学生子列表已按学号递增序排好序。
# 请设计一个程序，使用折半查找算法通过最少次数的比较找到指定学号的学生
# 如果有， 输出这个学生的学号和姓名， 如果没有， 输出报告未找到该学生。
number = eval(input())
stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
left = 0
right = len(stu_list) - 1
mid = (left + right) // 2
flag = False
for i in stu_list:
    if number in i[0]:
        flag = True
while left < right:
    if number in stu_list[mid]:
        print(stu_list[0]+stu_list[1])
    elif flag == False:               
                print("None")
                break
    else:
        index1 = stu_list.find(number)   
        if index1 < mid:
            right = mid -1
        else:
            left = mid + 1


