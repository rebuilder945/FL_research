def classify(x,ls):
	for n in ls:
	        if x < n:
	                'k1':[].append(n)
	        else:
	                'k2':[].append(n)
	return dic.append('k1','k2')

	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

