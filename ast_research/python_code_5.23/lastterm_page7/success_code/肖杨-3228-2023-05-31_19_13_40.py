def classify(x,ls):
	    t1 = ('k1',)
	    t2 = ('k2',)
	    t3 = []
	    t4 = []
	    for i in ls:
	        if i > x:
	            t3.append(i)
	        else:
	            t4.append(i)
	    t1 += (t3,)
	    t2 += (t4,)
	    dic.add(t1,t2)
	    a = tuple(dic)
	    return(a)
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

