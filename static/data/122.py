stu_list = [['201801', 'zhangyi'], ['201802', 'zhanger'], ['201803', 'zhangsan'], ['201804', 'zhangsi'],
             ['201805', 'wangyi'], ['201806', 'wanger'], ['201807', 'wangsan'], ['201808', 'wangsi'],
             ['201809', 'liyi'], ['201810', 'lier'], ['201811', 'lisan'], ['201812', 'lisi'],
             ['201813', 'zhaoyi'], ['201814', 'zhaoer'], ['201815', 'zhaosan'], ['201816', 'zhaosi'],
             ['201817', 'zhouyi'], ['201818', 'zhouer'], ['201819', 'zhousan'], ['201820', 'zhousi']]

a = stu_list

def binarySearch(s, v):
    begin, end = 0, len(s) - 1
    while begin <= end:
        mid = (begin + end) // 2
        if s[mid][0] == v:
            #s[mid] 是一个包含学生信息的列表，而 v 是一个整数，所以不能进行比较。
            print('stu_list[v]')
            break
        elif v > s[mid][0]:
            begin = mid + 1
        else:
            end = mid - 1
    else:
        print('None')

v = input()
binarySearch(a, v)

