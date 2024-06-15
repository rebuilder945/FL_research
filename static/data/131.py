a = eval(input())
lst = [['201801', 'zhangyi'], ['201802', 'zhanger'], ['201803', 'zhangsan'], ['201804', 'zhangsi'],
       ['201805', 'wangyi'], ['201806', 'wanger'], ['201807', 'wangsan'], ['201808', 'wangsi'],
       ['201809', 'liyi'], ['201810', 'lier'], ['201811', 'lisan'], ['201812', 'lisi'],
       ['201813', 'zhaoyi'], ['201814', 'zhaoer'], ['201815', 'zhaosan'], ['201816', 'zhaosi'],
       ['201817', 'zhouyi'], ['201818', 'zhouer'], ['201819', 'zhousan'], ['201820', 'zhousi']]
r = int(lst[0][0])
l = int(lst[-1][0])
#r 和 l 是从列表 list 中获取的日期字符串，因此它们是字符串类型，
#需要将它们转换为整数类型，以便可以对它们进行整数除法操作。
while r <= l:
    m = (r + l) // 2
    if lst[m][0] > a:
        r = m - 1
    elif lst[m][0] < a:
        l = m + 1
    elif lst[m][0] == a:
        print(m)
        break
else:
    print(None)
