def classify(x,ls):
	k1s=[]
	k2=[]
	for i in la:
	    if i>x:
	        k1s.append(i)
	    else:
	        k2s.append(i)
	dic=dict([("k1",k1s),("k2",k2s)])
	        
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

