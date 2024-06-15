def binary_search(stu_list, stu_id):    """
    left, right = 0, len(stu_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if stu_list[mid][0] == stu_id:
            return stu_list[mid]
        elif stu_list[mid][0] < stu_id:
            left = mid + 1
        else:
            right = mid - 1
    return None
stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
stu_id = input().strip()
result = binary_search(stu_list, stu_id)
if result:
    print("".join(result))
else:
    print("None")

