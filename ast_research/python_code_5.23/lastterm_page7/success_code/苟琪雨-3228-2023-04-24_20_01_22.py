def classify(x,ls):
	    ls1=[]
	    ls2=[]
	    for i in ls1:
	        if i>x:
	            ls1.append(i)
	    for n in ls2:
	        if n<=x:
	            ls2.append(n)
	    dic['k1']=ls1
	    dic['k2']=ls2

	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

