def classify(x,ls):
	    dic = {}
	    dic['k1'] = [i for i in ls if i > x]  # 大于x的值添加到k1对应的列表中
	    dic['k2'] = [i for i in ls if i <= x]  # 小于等于x的值添加到k2对应的列表中
	    return dic

	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

