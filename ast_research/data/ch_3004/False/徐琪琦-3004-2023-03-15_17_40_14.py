#读入一个自然数构成的列表，找出其中的每一个素数，然后放入另外一个列表，并输出这个列表。
list1 = eval(input())     #list不可以作为名称！
yushulist = []
list2 = []             #不要让list2 = list1然后之后用remove函数！因为list1会随着list2一起变
for x in list1:
    for i in range(2,int(pow(x,0.5))+1):         #学学！怎么找素数？从2到[根号x]都没有因子的就是素数
        yushulist.append(x % i)     #注意//不是取余数啊！
    if not 0 in list1:
        list2.extend([x])
print(list2)
