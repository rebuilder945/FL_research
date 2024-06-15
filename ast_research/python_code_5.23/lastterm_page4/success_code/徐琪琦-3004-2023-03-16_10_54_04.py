#读入一个自然数构成的列表，找出其中的每一个素数，然后放入另外一个列表，并输出这个列表。
list1 = eval(input())     #list不可以作为名称！
list2 = []             #不要让list2 = list1然后之后用remove函数！因为list1会随着list2一起变
if not 1 in list1 and not 0 in list1:
    for x in list1:
        yushulist = []  #不可以在line3定义这个余数list！！！
        for i in range(2,int(pow(x,0.5))+1):         #学学！怎么找素数？从2到[根号x]都没有因子的就是素数,别的方法：质数分布的规律：大于等于5的质数一定和6的倍数相邻。
            yushulist.append(x % i)     #注意//不是取余数啊！
        if not 0 in yushulist:
            list2.extend([x])
    print(list2)
else:
    while 1 in list1 or 0 in list1:
        list1.remove(1)
        list1.remove(0)
    for x in list1:
        yushulist = []  #不可以在line3定义这个余数list！！！
        for i in range(2,int(pow(x,0.5))+1):         #学学！怎么找素数？从2到[根号x]都没有因子的就是素数,别的方法：质数分布的规律：大于等于5的质数一定和6的倍数相邻。
            yushulist.append(x % i)     #注意//不是取余数啊！
        if not 0 in yushulist:
            list2.extend([x])
    print(list2)
