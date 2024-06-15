def classify(x,ls):
	m = {}
	n = []
	l = []
	for i in ls:
	    if i>x:
	       n.append(i)
	    else:
	        l.append(i)
	dic= {'k1':n,'k2',l}
	return dic
	
	        

	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

