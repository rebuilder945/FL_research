def classify(x,ls):
	    l1=[]
	    l2=[]
	    for i in ls:
	        if int(i) <=int(x):
	            l1.append(i)
	        else:
	            l2.append(i)
	    dic['k1']=l1
	    dic['k2']=l2
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

