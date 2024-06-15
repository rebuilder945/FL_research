def classify(x,ls):
	    select1 = []
	    select2 = []
	    for i in ls:
	        if i>x:
	            select1.append(i)
	        if i<=x:
	            select2.append(i)
	    select1 = ",".join(map(str,select1))
	    select2 = ",".join(map(str,select2))
	    dic['k1'] = select1
	    dic['k2'] = select2
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

