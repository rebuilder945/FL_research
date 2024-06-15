def classify(x,ls):
	def classify(x, ls):
	    # 初始化字典
	    dic = {'k1': [], 'k2': []}
	
	    # 遍历列表，将大于x的值保存至k1中，将小于等于x的值保存至k2中
	    for i in ls:
	        if i > x:
	            dic['k1'].append(i)
	        else:
	            dic['k2'].append(i)
	
	    # 返回分类后的字典
	    return dic

	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

