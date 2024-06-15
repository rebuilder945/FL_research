stu_list = [['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],
            ['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],
            ['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],
            ['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],
            ['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]

target = input()

left, right = 0, len(stu_list)-1  # 初始化查找区间
while left <= right:
    mid = (left + right) // 2  # 计算中间位置
    if stu_list[mid][0] == target:  # 找到目标元素
        print(stu_list[mid][0] + stu_list[mid][1])
        break
    elif stu_list[mid][0] < target:  # 目标元素在右侧区间
        left = mid + 1
    else:  # 目标元素在左侧区间
        right = mid - 1
else:  # 没有找到目标元素
    print(None)

