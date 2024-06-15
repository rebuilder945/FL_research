def classify(x,ls):
	    lis_big=[]
	    lis_little=[]
	    global dic
	    for i in ls:
	        i=int(i)
	        if i>x:
	            lis_big.append(i)
	        else:
	            lis_little.append(i)
	    dic={'k1':lis_big,'k2':lis_little}

	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

