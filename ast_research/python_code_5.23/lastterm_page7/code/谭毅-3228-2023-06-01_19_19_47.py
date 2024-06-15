def classify(x,ls):
	k1n=[]
	k2n=[]
	for n in ls:
	    if n>x:
	    k1n.append(x)
	    else:
	    k2n.apeend(x)
	dic{'k1','k2'}='k1n','k2n'
	    

	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

