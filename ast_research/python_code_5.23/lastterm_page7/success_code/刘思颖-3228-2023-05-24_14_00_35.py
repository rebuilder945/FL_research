def classify(x,ls):
	  dayu=[]
	  xiaoyu =[]
	  for i in ls:
	      if i>x:
	          dayu.append(i)
	      else :
	          xiaoyu.append(i)
	  dic['k1']=dic.get('k1',dayu)
	  dic['k2']=dic.get('k2',xiaoyu)
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

