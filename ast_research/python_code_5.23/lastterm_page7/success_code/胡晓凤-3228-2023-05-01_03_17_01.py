def classify(x,ls):
	def classify(x,ls):
	    dic={'k1':[],'k2':[]}
	    for i in ls:
	        if eval(i) <=x:
	            k1.append(i)
	        if eval(i) > x:
	            k2.append(i)
	        items=k1+k2
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

