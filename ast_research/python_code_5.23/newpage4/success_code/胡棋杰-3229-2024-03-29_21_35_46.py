from itertools import count


a=eval(input())
k=[]
for i in range(len(a)):
   b=a.count(a[i])
   if b ==1:
    k.append(a[i])
   else :
    continue
q=sorted(k,reverse=True)
q1=str(q)[1:-1]
print(q1)

#for n in range(len(q)):
    #=(q[n],end=(","))




  


