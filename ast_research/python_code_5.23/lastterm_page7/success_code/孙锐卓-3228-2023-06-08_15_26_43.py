def classify(x,ls):
	list_k1=[]
	list_k2=[]
	for i in range(len(ls)):
	    if ls[i] >x:
	        list_k1.append(ls[i])
	    else:
	        list_k2.append(ls[i])
	dic['k1']=list_k1
	dic['k2']=list_k2

	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

