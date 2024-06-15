def classify(x,ls):
	def classify(x,ls):
	    a1=[]
	    a2=[]
	    for i in ls:
	        if i>x:
	            a1.append(i)
	        else:
	            a2.append(i)
	    dic['k1']=a1
	    dic['k2']=a2
	x=int(input()) 

	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

