a=input().split(' ')
dic1={}
for i in a:
     if i in dic1:
          dic1[i]+=1
     else:
          dic1[i]=1
n=max(dic1.keys(),key=(lambda x:dic1[x]))
lis1=sorted(dic1.items(),key=lambda x:x[0])
for i in lis1:
     if i[1]==dic1[n]:
          print(i[0],i[1])
