def classify(x,ls):
	    k1 = []  # 用于存储所有大于 x 的元素
	    k2 = []  # 用于存储所有小于等于 x 的元素
	    for ele in ls:
	        if ele > x:
	            k1.append(ele)
	        else:
	            k2.append(ele)
	    res = {'k1': k1, 'k2': k2}  # 构造返回值，将两个列表保存在字典中
	    return res  # 返回字典
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

