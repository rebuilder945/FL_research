def classify(x,ls):
	k1=[]
	k2=[]
	for l in ls:
	    if l>x:
	        k1.append(l)    
	    else:
	        k2.append(l)
	dic['k1']=k1
	dic['k2']=k2
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

