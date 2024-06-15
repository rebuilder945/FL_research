def classify(x,ls):
	    ls1=[]
	    ls2=[]
	    for i in ls:
	        if i >x:
	            ls1.append(i)
	        else:
	            ls2.append(i)
	    dic1={}
	    dic2={}
	    dic1['k1']=ls1
	    dic2['k2']=ls2

	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

