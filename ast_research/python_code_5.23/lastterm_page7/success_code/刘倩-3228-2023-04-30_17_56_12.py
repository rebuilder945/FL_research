def classify(x,ls):
	dic = {'k1':[],'k2':[]}
	for k in ls:
	    if k>x :
	        dic['k1'].append(k)
	    else:
	        dic['k2'].append(k)
	return [(k, v) for k, v in dic.items()]
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

