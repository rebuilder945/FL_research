def classify(x,ls):
	n1 = []
	n2 = n1.copy()
	for y in ls:
	    if y>x:
	        n1.append(y)
	    else:
	        n2.append(y)
	dic['k1']=n1
	dic['k2']=n2
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

