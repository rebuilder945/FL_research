def classify(x,ls):
	"""
	    将所有大于x的值保存至字典的第一个key中，将小于等于x的值保存至第二个key的值中
	    Args:
	        - x: int，分类的中间值
	        - ls: List[int]，需要分类的列表
	    Returns:
	        - dict，字典，包含两个key，分别对应大于x和小于等于x的值列表
	    """
	    dic = {"k1": [], "k2": []}  # 初始化字典，两个key分别对应大于x和小于等于x的值列表
	    for num in ls:  # 遍历列表中的每个元素
	        if num > x:  # 如果大于x，添加到第一个key对应的值列表中
	            dic["k1"].append(num)
	        else:  # 否则，添加到第二个key对应的值列表中
	            dic["k2"].append(num)
	    return dic
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

