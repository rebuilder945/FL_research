def classify(x,ls):
	    key1=[]
	    key2=[]
	    for y in ls:
	        if y>x:
	            key1.append(y)
	        else:
	            key2.append(y)
	    dic['k1']=key1
	    dic['k2']=key2
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

