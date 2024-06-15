lst=eval(input())
n,m=map(int,input().split(","))
lst2=[]
for i in range(len(lst)):
  if n>len(lst):
    print("error")
    break
  elif n<=len(lst):
    if i==n:
      lst2.append(lst[i])
      lst2=lst2*m
      lst2[0:0]=lst
      print(lst2)
    else:
      print("error")
  
