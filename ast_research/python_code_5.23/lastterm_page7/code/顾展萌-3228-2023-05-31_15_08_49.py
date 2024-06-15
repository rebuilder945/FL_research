def classify(x,ls):
	d = {"k1": [], "k2": []}
	    for i in ls:
	        if i > x:
	            d["k1"].append(i)
	        else:
	            d["k2"].append(i)
	    
	    return [(key, [(i, ls.index(i)) for i in d[key]]) for key in d.keys()]
	   
	  
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

