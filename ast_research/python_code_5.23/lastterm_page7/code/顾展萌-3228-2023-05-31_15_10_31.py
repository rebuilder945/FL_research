def classify(x,ls):
	d = {"k1": [], "k2": []}
	    for i in ls:
	        if i > x:
	            d["k1"].append(i)
	        else:
	            d["k2"].append(i)
	    # 将字典转换为列表并按照key排序
	    res = [(key, d[key]) for key in sorted(d.keys())]
	    return res
	  
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

