num = eval(input())
stu_list = [['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],
['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],
['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],
['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],
['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
nLen = len(stu_list) - 1
sta = 0
end = nLen
mid = (sta + end) // 2
while sta < end:
    if num == stu_list[mid][1]:
        print(",".join(stu_list[mid]))
        break
    elif num > stu_list[mid][1]:
        sta = mid + 1
    else:
        end = mid - 1
    mid = (sta + end) // 2
print("None")
