def classify(x,ls):
	dic["k1"]=str(i for i in ls if i >x)
	dic["k2"]=str(t for t in ls if t<=x)
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

