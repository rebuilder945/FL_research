def classify(x,ls):
	   for i in range(0,len(ls)+1):
	     if ls[i]>x:
	        dic['k1']=ls[i]
	     else :
	        dic['k2']=ls[i]
	   
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

