def classify(x,ls):
	    dic={'k1':'','k2':''}
	    for i in range (len(ls)):
	        if ls[i]>x:
	            dic['k1'].append(ls[i])
	        elif ls[i]<=x:
	            dic['k2'].append(ls[i])
	    return(dic)
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

