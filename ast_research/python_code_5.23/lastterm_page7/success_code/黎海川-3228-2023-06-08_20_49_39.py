def classify(x,ls):
	s = {"k1":[],"k2":[]}
	for i,j in enumerate(ls,0):
	    if i <= x:
	        s["k2"].append(i)
	    else:
	        s["k1"].append(j)
	    return s
	    
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

