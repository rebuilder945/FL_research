def classify(x,ls):
	ls1=[]
	ls2=[]
	for y in ls:
	    if y > x:
	        ls1.appemd(y)
	    else:
	        ls2.append(y)
	dic["k1"]=dic.get("k1",ls1)
	dic["k2"]=dic.get("k2",ls2)
	    
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

