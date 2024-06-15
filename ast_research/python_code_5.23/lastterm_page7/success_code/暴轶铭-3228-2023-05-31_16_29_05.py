def classify(x,ls):
	dic = {"k1": [], "k2": []}  #初始化字典，两个key分别对应大于x和小于等于x的值列表
	for x in ls:  # 遍历列表中的每个元素
	    if x > x:  #如果大于x，添加到第一个key对应的值列表中
	        dic["k1"].append(x)
	    else:  # 否则，添加到第二个key对应的值列表中
	        dic["k2"].append(x)
	return dic
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

