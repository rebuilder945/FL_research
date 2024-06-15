def classify(x,ls):
	key1=[]
	key2=[]
	for i in ls:
	    if i >x:
	        key1.append(i)
	    else:
	        key2.append(i)
	    dic={'k1',key1,'k2',key2}
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

