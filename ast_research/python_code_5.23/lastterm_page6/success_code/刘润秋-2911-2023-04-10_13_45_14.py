ls1=input()
ls2=[]
for i in range(len(ls1)):
    ls2.append(int(ls1[i]))
for j in range(len(ls2)):
    ls2[j]=(ls2[j]+5)%10
ls3=ls2[::-1]
for k in range(len(ls3)):
   print(ls3[k],end='')
