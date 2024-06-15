def classify(x,ls):
	list1 = []
	    list2 = [] 
	    for i in range(len(ls)):
	        if i > x:
	            list1.append(i)  
	        elif i <= x:
	            list2.append(i)
	    dic = {"k1":list1,"k2":list2}
	    print(dic)
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

