def classify(x,ls):
	for y in ls:
	    lst1=[]
	    lst2=[]
	    if y >x:
	         lst1.append(y)
	    else:
	         lst2.append(y)
	dic['k1']=lst1
	dic['k2']=lst2

	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

