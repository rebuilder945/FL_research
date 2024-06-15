def classify(x,ls):
	dic = {"k1": [], "k2": []}
	for num in ls:
	    num = int(num.strip("'"))
	    if num > x:
	        dic.setdefault('k1', []).append(num)
	    else:
	        dic.setdefault('k2', []).append(num)
	return dic
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

