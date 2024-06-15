def classify(x,ls):
	dic1 = {'k1':[],'k2':[]}
	for k in ls:
	    if k>x :
	        dic1['k1'].append(k)
	    else:
	        dic1['k2'].append(k)
	return dic1.items()
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

