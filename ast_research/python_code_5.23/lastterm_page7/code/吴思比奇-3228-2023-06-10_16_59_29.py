def classify(x,ls):
	
	
	 n1=[]
	 n2=[]
	dir={}
	for i in ls:
	
	    if i >x:
	
	        n1.append(i)
	
	    else:
	
	        n2.append(i)
	
	    dir["k1"]=n1
	
	    dir["k2"]=n2
	
	a=set(dir)
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

