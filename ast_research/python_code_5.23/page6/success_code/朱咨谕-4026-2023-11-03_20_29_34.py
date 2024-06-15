#2/1, 3/2, 5/3, 8/5, 13/8, 21/13,.
lst=[]
for i in range(0,100):
    lst.append(i)
lst[0]=1
lst[1]=2
lst[2]=3
for i in range(3,100):
    lst[i]=lst[i-1]+lst[i-2]
tot=0
n=eval(input())
for i in range(0,n):
    tot+=lst[i+1]/lst[i]
print("%.4f"%tot)
#print(lst)
