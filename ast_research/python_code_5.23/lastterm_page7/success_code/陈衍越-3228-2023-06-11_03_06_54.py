def classify(x,ls):
	    lst1 = [i for i in ls if i > x]
	    lst2 = [i for i in ls if x >= i]
	    #将lst1装入k1，lst2装入k2
	    dic["k1"] = lst1
	    dic["k2"] = lst2
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

