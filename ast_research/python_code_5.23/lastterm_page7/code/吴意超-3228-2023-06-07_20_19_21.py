def classify(x,ls):
	dic = {"even": [], "odd": []}
	    for i in range(x):
	        if ls[i] % 2 == 0:
	            dic["even"].append(ls[i])
	        else:
	            dic["odd"].append(ls[i])
	    return dic
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

