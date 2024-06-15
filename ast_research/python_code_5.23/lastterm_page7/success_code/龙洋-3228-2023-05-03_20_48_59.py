def classify(x,ls):
	    li1=[]
	    li2=[]
	    for n in ls:
	        if n>x:
	            li1.append(n)
	        else:
	            li2.append(n)
	    dic['k1']=li1
	    dic['k2']=li2
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

