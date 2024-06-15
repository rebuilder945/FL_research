def classify(x,ls):
	    k1n=[]
	    k2n=[]
	    for i in ls:
	        if i > x:
	            k1n.append(i)
	        else:
	            k2n.append(i)
	    dic["k1","k2"]=k1n,k2n
	    return dic
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

