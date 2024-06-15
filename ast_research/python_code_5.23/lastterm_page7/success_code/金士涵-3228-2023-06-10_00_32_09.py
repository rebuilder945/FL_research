def classify(x,ls):
				    lst=[]
				    lst2=[]
				    lst3=["k1","k2"]
				    for i in ls:
				        if i>x:
				            lst.append(i)
				        elif i<=x:
				            lst2.append(i)
				    dic[lst3[0]]=lst
				    dic[lst3[1]]=lst2
				    lst4=list(dic.items())
				    return lst4
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

