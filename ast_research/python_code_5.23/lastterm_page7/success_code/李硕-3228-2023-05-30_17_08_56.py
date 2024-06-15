def classify(x,ls):
	k1 = []
	k2 = []
	for ele in ls:
	      if ele > x:
	          k1.append(ele)
	      else:
	          k2.append(ele)
	rest = {'k1': k1, 'k2': k2}
	return rest
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

