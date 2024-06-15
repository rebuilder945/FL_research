def classify(x,ls):
	k1ls=[]
	k2ls=[]
	for k in ls:
	    if k>x:
	        k1ls.append(k)
	    else:
	        k2ls.append(k)
	dic1={}
	dic1['k1']=k1ls
	dic1['k2']=k2ls
	return dic=dic1

	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

