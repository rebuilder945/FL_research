def classify(x,ls):
	v1=[]
	v2=[]
	for i in ls:
	    if i>x:
	        v1.append(i)
	    else:
	        v2.append(i)
	dic["k1"]=v1
	dic["k2"]=v2
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

