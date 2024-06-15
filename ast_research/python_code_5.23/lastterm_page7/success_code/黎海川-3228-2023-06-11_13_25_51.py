def classify(x,ls):
	m=[]
	n=[]
	for i in ls:
	    if i > x:
	        m.append(i)
	    if i <= x:
	        n.append(i)
	dic.setdefault('k1',m)
	dic.setdefault('k2',n)

	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

