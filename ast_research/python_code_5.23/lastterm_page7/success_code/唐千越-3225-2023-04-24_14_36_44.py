def work(a) :
     jc = 1
     jclst=[1]
     for i in range(1,a+1):
           jc *=1
           jclst.append(jc)
           ans=dict(i,jclst)
     print(ans)
    
           
	

a = int(input())
ans = work(a)
print(ans)

