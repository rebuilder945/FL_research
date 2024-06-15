def classify(x,ls):
	for num in ls:
	    if num > x:
	        dic['k1'].append(num)  # 将大于x的值添加到字典的'k1'键对应的列表中
	    else:
	        dic['k2'].append(num)  # 将小于等于x的值添加到字典的'k2'键对应的列表中
	
	return 
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

