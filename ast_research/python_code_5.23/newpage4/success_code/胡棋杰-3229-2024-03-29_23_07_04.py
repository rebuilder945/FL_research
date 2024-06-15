from itertools import count 


a=eval(input())
k=[]
g=[]
num=0
for i in range(len(a)):
    b=a.count(a[i])
    if b==1:
     k.append(a[i])
     num+=1
    else:
     continue
if num==0:
  print("False")
else:
  q=sorted(k)
  q1=str(q)[1:-1]
  print(q1.replace(" ",""))
#q2=q1.split(",")
#print(q2)


    

