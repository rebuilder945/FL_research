def classify(x,ls):
	sText1='k1'
	sText='k2'
	for i in ls:
	    if i >x:
	        sText1+=(i+",")
	    else:
	        sText2+=(i+",")
	items=[('k1',k1),('k2',k2)]
	return items
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

