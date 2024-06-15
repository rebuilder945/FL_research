ls=eval(input())
n,m=eval(input())
ls2=[]
if n<len(ls):
    a=ls[n]
    ls.remove(a)
    ls2.append(a)
    ls3=ls2*m
    print(ls+ls3)
else:
    print("error")


        

            


        
