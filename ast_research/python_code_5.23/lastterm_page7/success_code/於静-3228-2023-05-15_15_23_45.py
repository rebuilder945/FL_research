def classify(x,ls):
	k1=lst1=[]
	k2=lst2=[]
	for i in range(1,len[ls]):
	    if ls[i] > x:
	        lst1.append(ls[i])
	    else:
	        lst2.append(ls[i])
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

