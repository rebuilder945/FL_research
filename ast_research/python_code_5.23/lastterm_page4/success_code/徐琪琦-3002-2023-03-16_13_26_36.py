#输入一个整数列表，计算所有元素的平均值，如果结果中小数为0，请只输出整数部分，如果结果中的小数部分不为0，则输出结果保留两位小数。
list1 = eval(input())
avg = float(sum(list1)/len(list1))
if list(str(avg).split("."))[1] == "0":         #列表里面字符串，所以一定0旁边要加上引号
    print(int(avg))
else:
    print("%.2f"%avg)
