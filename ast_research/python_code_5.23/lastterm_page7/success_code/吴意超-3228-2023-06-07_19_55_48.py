def classify(x,ls):
	def classify(x,ls):
	    result = {'k1': [], 'k2': []}  # 构造一个空字典，初始化两个key对应的值均为空列表
	    for num in ls:  # 遍历列表中的每一个数值
	        if num > x:  # 如果当前数值大于x，则将其添加到第一个key对应的值中
	            result['k1'].append(num)
	        else:  # 否则将其添加到第二个key对应的值中
	            result['k2'].append(num)
	    return [(k, result[k]) for k in result]  # 将字典转换为列表，并输出
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

