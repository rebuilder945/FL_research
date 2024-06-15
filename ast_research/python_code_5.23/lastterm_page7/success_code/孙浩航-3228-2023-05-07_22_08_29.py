def classify(x,ls):
	    key1="k1"
	    key2="k2"
	    for i in ls:
	        if i <= x:
	            dic.setdefault ( key2, []).append ( i)
	        else:
	            dic.setdefault ( key2, []).append ( i)
	    return dic
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

