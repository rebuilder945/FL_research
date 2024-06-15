def classify(x,ls):
	    b1=[]
	    b2=[]
	    for i in ls:
	        if i>x:
	            b1.append(i)
	        else:
	            b2.append(i)
	    dt={'k1':b1,'k2':b2}
	    return dt
	    
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

