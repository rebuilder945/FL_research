def classify(x,ls):
	s = {}
	for i in ls:
	    if int(i) <= x:
	        s.setdefault('k2',i)
	for j in ls:
	    if int(j) <= x:
	        s.setdefault('k1',j)
	    return s
	    
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

