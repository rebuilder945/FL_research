# #1
# def classify(x,ls):
#     lst1=[]
#     lst2=[]
#     for i in ls:
#         if i<x:
#             lst2.append(i)
#         elif i>x:
#             lst1.append(i)
#     dic['k1']=lst1
#     dic['k2']=lst2


# x  =  int(input())
# ls  =  input().split()
# ls  =  list(map(int,ls))  #  map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
# dic  =  {}
# classify(x,ls)

# print(sorted(list(dic.items())))

# #2
# def  work(a)  :
#     dic={}
#     for i in range(a+1):
#         if i == 0:
#             dic[i]=1
#         else:
#             n=1
#             for x in range(1,i+1):
#                 n*=x
#             dic[i]=n
#     return dic

# a  =  int(input())
# ans  =  work(a)
# print(ans)

# #3
# item  =  input()  or  "None"
# goods  =  {}
# while(item  !="None"):
#         name,  cost  =  item.split()
#         cost  =  eval(cost)
#         goods[name]  =  cost
#         item  =  input()  or  "None"

# goodsNum  = len(goods)

# money=0
# for  i  in  goods:
        
#     money+=goods[i]


# print(goodsNum,"%.2f"%(money))

'''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''
# #1
# s = input()or'q'
# dic={}
# while s!='q':
#     a=dic.get(s)
#     if a==None:
#         dic[s]=1
#     else:
#         dic[s]+=1
#     s = input()or'q'
# lst = []
# for x,y in dic.items():
#     lst+=[[y,x]]
# lst.sort()
# print(lst[-1][-1],lst[-1][0])

# #2
# lst=input().split()
# dic={}
# lst1=[]
# for i in lst:
#     dic[i]=dic.get(i,0)+1
# for x,y in dic.items():
#     lst1.append([x,y])
# lst1.sort()
# lst1.sort(key = lambda x:x[1],reverse=True)
# a=lst1[0][1]
# for n in lst1:
#     if n[1]==a:
#         print(n[0],n[1])
   
#3
a,*b = input().split()
lst=b
for i in range(len(lst)):
    lst[i] = eval(lst[i])
lst.sort(reverse= True)
print(a,'%.2f %.2f %.2f %.2f'%(lst[0],lst[1],lst[2],sum(lst)/len(lst)))

