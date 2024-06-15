def classify(x,ls):
	for i in range(ls(len)):
	    if ls[i]>x:
	        dict['k1']=ls[i]
	    else :
	        dict['k2']=ls[i]
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

