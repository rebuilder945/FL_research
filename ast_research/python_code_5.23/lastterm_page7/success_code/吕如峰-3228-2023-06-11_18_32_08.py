def classify(x,ls):
	    dict1={'k1': [], }
	    dict2={'k2': []}
	    for n in ls:
	        if x < n:
	            dict1.append(n)
	        else:
	            dict2.append(n)
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

