def classify(x,ls):
	# def  work(a) :
	#     dic={}
	#     for i in range(a+1):
	#         b=1
	#         for x in range(i):
	#             b*=x+1
	#         dic[i]=b
	#     return(dic)
	# a  =  int(input())
	# ans  =  work(a)
	# print(ans)
	
	# item  =  input()  or  "None"
	# goods  =  {}
	# while(item  !="None"):
	#         name,  cost  =  item.split()
	#         cost  =  eval(cost)
	#         goods[name]  =  cost
	#         item  =  input()  or  "None"
	# goodsNum  =len(goods)
	# money=0
	# for  i  in  goods:        
	#     money+=goods[i]
	#     print(money)
	# print(goodsNum,"%.2f"%(money)
	
	# a=input() or "q"
	# dic={}
	# for line in a:
	#     while(a !="q"):
	#         b=a
	#         dic[b]=dic.get(b,0)+1
	# list=[]
	# for k,v in dic.items():
	#     list.append([k,v])
	# print(list)
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

