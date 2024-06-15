A=eval(input())
A.sort()
B=[]
for i in range(len(A)):
    if A.count(A[i])==1:
       B.append(A[i])
if B!=[]:
  print(','.join(map(str,B)))
else:
  print(False)


