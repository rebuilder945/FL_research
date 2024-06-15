def classify(x,ls):
	def classify(x,ls):
	    a1=[]
	    a2=[]
	    for i in ls:
	        if i>x:
	            a1.append(i)
	        else:
	            a2.append(i)
	    ls1={}
	    ls1['k1']=a1
	    ls1['k2']=a2
	    return ls1
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

