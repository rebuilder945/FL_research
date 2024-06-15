lis=list(map(int,input().split(",")))
n,m=eval(input())
if(n<-len(lis) or n>=len(lis)):
      print("error")
else:
      temp=[lis[n] for i in range(0,m)]
      print(lis+temp)
