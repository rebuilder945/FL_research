def classify(x,ls):
	k01=[]
	k02=[]
	for i in ls:
	    if i>x:
	        k01.append(i)
	    else:
	        k01.append(i)
	items=[('k1',k01),('k2',k02)]

	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

