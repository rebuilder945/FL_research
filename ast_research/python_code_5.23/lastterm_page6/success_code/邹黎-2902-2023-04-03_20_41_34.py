num=eval(input())
lst1=[1,2]
lst2=[]
result=0
for x in range(1,num):
    a=lst1[x]+lst1[x-1]
    lst1.append(a)
for x in range(num):
    lst2.append(lst1[x+1])
for x in range(1,len(lst2)+1,1):
    result+=(lst2[x-1]/lst1[x-1])
print("%.4f"%result)
