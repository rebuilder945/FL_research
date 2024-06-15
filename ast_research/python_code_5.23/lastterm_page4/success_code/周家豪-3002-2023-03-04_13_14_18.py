# 输入一个整数列表，计算所有元素的平均值，如果结果中小数为0，
# 请只输出整数部分，如果结果中的小数部分不为0，则输出结果保留两位小数。

list=eval(input())
sum=sum(list)
average=sum/len(list)

if average==int(average):
    print(int(average))
else:
    print("%.2f"%(average))


