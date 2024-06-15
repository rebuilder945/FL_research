def classify(x,ls):
	zidian = {}
	dayu = []
	xiaoyu = []
	for i in list:
	if i>66:
	dayu.append(i)
	elif i<66:
	xiaoyu.append(i)
	zidian[“大于66的”] = dayu
	zidian[“小于66的”] = xiaoyu
	print(zidian)

	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

