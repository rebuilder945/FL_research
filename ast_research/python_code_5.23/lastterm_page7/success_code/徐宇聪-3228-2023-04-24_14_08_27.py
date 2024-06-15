def classify(x,ls):
	for i in range(len(ls)):
	        if ls[i] > x:
	            ls1 = []
	            ls1.append(ls[i])
	        else:
	            ls2 = []
	            ls2.append(ls[i])
	dic['k1'] = ls1
	dic['k2'] = ls2
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

