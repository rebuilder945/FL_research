def classify(x,ls):
	num1=[]
	num2=[]
	for i in ls:
	    if i >x:
	        num1.append(i)
	    else:
	        num2.append(i)
	dic['k1']=num1
	dic['k2']=num2
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

