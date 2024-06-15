def max_number(a):
    a.sort(reverse=True) #对列表a进行排序,sort用来排序，后面那个reserve=true是降序排序
    b = '' #创造一个空字符串
    for c in a: #遍历排序后的数字列表
        b += str(c) #把每个数字都转化为字符串，并添加到c中
    return int(b) #将最后字符串转换成整数并返回

a = [0, 1, 2, 3, 2]
print(max_number(a))
