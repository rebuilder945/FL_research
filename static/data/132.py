ls = [['201801', 'zhangyi'], ['201802', 'zhanger'], ['201803', 'zhangsan'], ['201804', 'zhangsi'],
      ['201805', 'wangyi'], ['201806', 'wanger'], ['201807', 'wangsan'], ['201808', 'wangsi'],
      ['201809', 'liyi'], ['201810', 'lier'], ['201811', 'lisan'], ['201812', 'lisi'],
      ['201813', 'zhaoyi'], ['201814', 'zhaoer'], ['201815', 'zhaosan'], ['201816', 'zhaosi'],
      ['201817', 'zhouyi'], ['201818', 'zhouer'], ['201819', 'zhousan'], ['201820', 'zhousi']]

a = eval(input())
if 201800 < a < 201821:
    for i in ls:
        t = i[0]
        #问题在于尝试将字符串 t 的第一个字符（即 t[0]）赋值给变量 h，然后又尝试将其转换为整数类型，
        #但是，由于 t 是一个列表中的元素，因此 t[0] 实际上是列表中的另一个列表，而不是字符串，因此不能直接进行索引操作。
        h = int(t[:4])  # 提取年份部分并转换为整数
        if a == h:
            print(i[0] + i[-1])
else:
    print("None")