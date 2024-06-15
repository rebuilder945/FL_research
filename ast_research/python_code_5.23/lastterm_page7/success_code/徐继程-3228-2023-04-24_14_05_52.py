def classify(x,ls):
	list1=[]
	list2=[]
	for i in ls:
	    if x>=i:
	        list2.append(i)
	    else:
	        list1.append(i)
	dic.update({'k1':list1,'k2':list2})
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

