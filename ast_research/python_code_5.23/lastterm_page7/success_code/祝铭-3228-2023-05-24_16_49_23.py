def classify(x,ls):
	l1 = []
	l2 = []
	dic = {}
	for i in range(len(ls)):
	    if ls[i] > x :
	        l2.append(ls[i])
	    else:
	        l1.append(ls[i])
	dic['k1'] = l2
	dic['k2'] = l1
	print(dic)
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

