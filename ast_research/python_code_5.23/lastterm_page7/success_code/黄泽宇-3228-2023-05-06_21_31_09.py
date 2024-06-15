def classify(x,ls):
	    alist=[]
	    blist=[]
	    for i in ls:
	        if i > x:
	            alist.append(i)
	        else:
	            blist.append(i)
	    dic['k1']=alist
	    dic['k2']=blist
	  
	   
	
	    
	  
	
x = int(input())
ls = input().split()
ls = list(map(int,ls)) # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x,ls)

print(sorted(list(dic.items())))

