def classify(x,ls):
	listk1=[]
	listk2=[]
	for m in ls:
	    if m>x:
	        listk1.append(m)
	    else:
	        listk2.append(m)
	dic['key1']=listk1
	dic['key2']=listk2
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

