def classify(x,ls):
	    for a in ls:
	        if a > x:
	            i = ls.index(a)
	            break
	    dic['k1'] = ls[i:]
	    dic['k2'] = ls[:i]
	    return dic
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

