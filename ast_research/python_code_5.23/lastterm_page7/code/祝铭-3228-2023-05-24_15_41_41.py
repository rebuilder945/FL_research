def classify(x,ls):
	l1 = []
	l2 = []
	l3 = ['k1','k2']
	for i in ls:
	    if ls[i] > x :
	        l2.append(ls[i])
	    else:
	        l1.append(ls[i])
	l4 = [l1,l2]
	print(dict(zip(l3,l4)
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

