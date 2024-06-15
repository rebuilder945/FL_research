def classify(x,ls):
	for i in li:
	&#160;&#160;&#160;&#160;if i ==66: continue
	&#160;&#160;&#160;&#160;if i > 66:
	&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;list_1.append(i)
	&#160;&#160;&#160;&#160;else:
	&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;list_2.append(i)
	dic.setdefault('k1',list_1)
	dic.setdefault('k2',list_2)
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

