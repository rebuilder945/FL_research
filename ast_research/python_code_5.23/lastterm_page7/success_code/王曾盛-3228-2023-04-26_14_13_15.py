def classify(x,ls):
	
	    res_dict = {'k1': [], 'k2': []}
	    for num in ls:
	        if num > x:
	            res_dict['k1'].append(num)
	        else:
	            res_dict['k2'].append(num)
	    return [res_dict['k1'], res_dict['k2']]

	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

