def classify(x,ls):
	b=[]
	c=[]
	for i in ls:
	    if i > x:
	        b.append(i)
	    else:
	        c.append(i)
	B=('k1',b)
	C=('k2',c)
	D={B,C}
	return(D)
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

