def classify(x,ls):
	        dic={"k1":0,"k2":0}
	        for i in ls:
	            if i > x:
	                dic["k1"]=dic["k1"]+1
	            else:
	                dic["k2"]=dic["k2"]+1
	            return(dic)
	                
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

