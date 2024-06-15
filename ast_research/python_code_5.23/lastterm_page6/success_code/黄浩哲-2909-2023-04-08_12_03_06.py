stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]

while True:
    target = input()  # 要查找的学号
    if target == "stop":
        break
    left = 0  # 左边界
    right = len(stu_list) - 1  # 右边界

    while left <= right:
        mid = (left + right) // 2  # 中间位置
        if stu_list[mid][0] == target:  # 找到了
            print(stu_list[mid][0] + stu_list[mid][1])
            break
        elif stu_list[mid][0] < target:  # 在右半部分
            left = mid + 1
        else:  # 在左半部分
            right = mid - 1
    else:  # 没找到
        print("None")

