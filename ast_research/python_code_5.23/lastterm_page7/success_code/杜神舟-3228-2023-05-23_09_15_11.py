def classify(x,ls):
	
	    ls2=[]
	    ls3=[]
	    for y in ls:
	        if int(y)<=x:
	            ls2.append(int(y))
	        else:
	            ls3.append(int(y))
	    
	    dic['k1']=ls3
	    dic['k2']=ls2
	    
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

