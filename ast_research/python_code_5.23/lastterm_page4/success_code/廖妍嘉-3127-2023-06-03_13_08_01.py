n=int(input())
ls=[x for x in range(1,n+1)]
a=ls[0]
ls.remove(a)
ls.insert(-1,a)
ls[-1],ls[-2]=ls[-2],ls[-1]
print(ls)

            


        
