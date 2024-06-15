def classify(x,ls):
	b1 =[]
	b2 =[]
	for i in  ls:
	    if i > x:
	        b1.append(i)
	    if i < x:
	        b2.append(i)
	b = {"k1": b1}
	b["k2"] = b2
	return b

	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

