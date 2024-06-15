def work(a) :
     dic={}
     jiecheng=1
     for i in range(a+1):
          if i==0:
               dic[0]=1
          else:
               jiecheng=jiecheng*i
               dic[I]=jiecheng
     return dic
	

a = int(input())
ans = work(a)
print(ans)

