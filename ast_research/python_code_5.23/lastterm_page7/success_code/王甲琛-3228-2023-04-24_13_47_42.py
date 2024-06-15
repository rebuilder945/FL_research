def classify(x,ls):
	    lst1=[]
	    lst2=[]
	    for i in range (len(ls)):
	        if ls[i]>x:
	            lst1.append(len[i])
	        else:
	            lst2.append(len[i])
	    dic=dict(k1=lst1,k2=lst2)
	    print(dic)
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

