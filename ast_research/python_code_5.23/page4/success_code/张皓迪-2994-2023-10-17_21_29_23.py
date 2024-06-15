ls=list(map(int,input().split(',')))
n,m=eval(input())
a=[]
if n<-len(ls) or n>len(ls):
    print("error")
    
else:
    temp=[ls[n]for i in range(0,m)]
    print(ls+temp)

