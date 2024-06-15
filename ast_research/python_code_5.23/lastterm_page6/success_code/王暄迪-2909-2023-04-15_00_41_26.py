stu_list =[['201801', 'zhangyi'],
           ['201802', 'zhanger'],
           ['201803', 'zhangsan'],
           ['201804', 'zhangsi'],
           ['201805', 'wangyi'], ['201806', 'wanger'], ['201807', 'wangsan'], ['201808', 'wangsi'],
 ['201809', 'liyi'], ['201810', 'lier'], ['201811', 'lisan'], ['201812', 'lisi'],
 ['201813', 'zhaoyi'], ['201814', 'zhaoer'], ['201815', 'zhaosan'], ['201816', 'zhaosi'],
 ['201817', 'zhouyi'], ['201818', 'zhouer'], ['201819', 'zhousan'], ['201820', 'zhousi']]
 
search_no = int(input(''))
while 1:
    half_value = stu_list[int(len(stu_list)/2)]
    if int(half_value[0]) < search_no:
        stu_list = stu_list[int(len(stu_list)/2):]
    elif int(half_value[0]) == search_no:
        print(half_value)
        break
    else:
        stu_list = stu_list[:int(len(stu_list)/2)]
    if len(stu_list)<=1:
        print(None)
        break
