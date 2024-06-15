def classify(x,ls):
	    dic = {}
	    dic['k1'] = [i for i in ls if i > x]  # 大于x的值添加到k1对应的列表中
	    dic['k2'] = [i for i in ls if i <= x]  # 小于等于x的值添加到k2对应的列表中
	    return dic
	
	# 样例输入
	x = 66
	ls = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
	
	dic = classify(x, ls)
	
	# 把字典按照键值排序，并且转换成元组列表
	result = sorted(list(dic.items()))
	
	print(result)
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

