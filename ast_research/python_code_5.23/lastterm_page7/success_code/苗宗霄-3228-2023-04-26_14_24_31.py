def classify(x,ls):
	    dic = {"k1": [], "k2": []}  # 初始化一个空字典，其中k1表示大于x的值列表，k2表示小于等于x的值列表
	    for num in ls:
	        if num > x:  # 将大于x的数添加到k1对应的列表中
	            dic["k1"].append(num)
	        else:  # 将小于等于x的数添加到k2对应的列表中
	            dic["k2"].append(num)
	    return list(dic.items())  # 返回字典的键值对转换成的元组列表

	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

