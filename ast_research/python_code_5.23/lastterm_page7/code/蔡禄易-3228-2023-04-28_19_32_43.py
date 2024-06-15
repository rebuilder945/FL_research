def classify(x,ls):
	dayu = []
	xiaoyu = []
	for i in is:
	    if i > x:
	        dayu.append(i)
	    if i <= x:
	        xiaoyu.append(i)
	c = "k1"+dayu+"k2"+xiaoyu
	dic = dict(c)
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

