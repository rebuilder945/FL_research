def classify(x,ls):
	    larger = []
	    smaller = []
	    for num in ls:
	        if num > x:
	            larger.append(num)
	        else:
	            smaller.append(num)
	    return [('k1', larger), ('k2', smaller)]
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

